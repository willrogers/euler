#!/bin/bash

PROBLEMS=010
LOG=compile.log
rm $LOG

type=$1
PDIR=$1
LIBS=$PDIR/Utils.hs

function compile_python {
	if [ -f $PDIR/p$1.py ] ; then
		return 0 
	else
		return 1
	fi
}

function run_python {
	python $PDIR/p$1.py 2>> $LOG
}

function compile_haskell {
	if [ -f $PDIR/p$1.hs ] ; then
		ghc $PDIR/p$1.hs -i $LIBS >> $LOG 2>&1
		return $?
	else
		return 1
	fi
}

function compile_c {
	if [ -f $PDIR/p$1.c ] ; then
		gcc -o $PDIR/p$1 $PDIR/p$1.c -lm >> $LOG 2>&1
		return $?
	else
		return 1
	fi
}
function run_c {
	$PDIR/p$1
}

function run_haskell {
	$PDIR/p$1
}


correct=0
for x in $(seq -w $PROBLEMS) ; do
	if eval "compile_$type $x"; then
		st=$(date +%s)
		if ans=$(eval "run_$type $x") ; then 
		
			end=$(date +%s)
			duration=$(echo "$end-$st" | bc)
			printf "Problem %3d: answer %12d " $(expr $x + 0) $ans 
			result=incorrect
			if ./checker.py $x $ans ; then 
				result=correct
				((correct=correct+1))
			fi
			printf "%10s %3ds\n" $result $duration
		else
			echo "Problem $x: runtime error"
		fi
	fi
done


echo "$correct problems solved"
