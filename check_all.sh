#!/bin/bash

PROBLEMS=400
LOG=compile.log
DATADIR='./data'

if [ -f $LOG ] ; then
	rm $LOG
fi

if [ -z $1 ] || [ ! -d $1 ] ; then
	echo "Usage: $0 <lang>"
	exit
fi

LANG=$1
PDIR=$LANG
LIBS=$PDIR/Utils.hs

function compile_python {
	if [ -f $PDIR/p$1.py ] ; then
		return 0
	else
		return 1
	fi
}

function run_python {
	pypy $PDIR/p$1.py 2>> $LOG
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
	$PDIR/p$1 $DATADIR
}

function run_haskell {
	$PDIR/p$1
}

NUM_REGEX="^-?[0-9]+$"

start=$(date +%s)
correct=0
for x in $(seq -w $PROBLEMS) ; do
	if eval "compile_$LANG $x"; then
		st=$(date +%s)
		if ans=$(eval "run_$LANG $x") ; then 
			if ! [[ $ans =~ $NUM_REGEX ]] ; then
				printf "Problem %3d: not a number\n" $(expr $x + 0)
			else
				end=$(date +%s)
				duration=$(echo "$end-$st" | bc)
				printf "Problem %3d: answer %12d " $(expr $x + 0) $ans 
				result=incorrect
				if ./checker.py $x $ans ; then 
					result=correct
					((correct=correct+1))
				fi
				printf "%10s %3ds\n" $result $duration
			fi
		else
			printf "Problem %3d: runtime error\n" $(expr $x + 0)
		fi
	fi
done


end=$(date +%s)
duration=$(echo "$end-$start" | bc)
echo "$correct problems solved in ${duration}s"
