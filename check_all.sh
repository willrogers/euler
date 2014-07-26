#!/bin/bash

PROBLEMS=400
PDIR=haskell
LOG=compile.log
LIBS=$PDIR/Utils.hs
rm $LOG

correct=0
for x in $(seq -w $PROBLEMS) ; do
	if [ -f $PDIR/p$x.hs ] && ghc $PDIR/p$x.hs -i $LIBS >> $LOG 2>&1 ; then
		start=$(date +%s)
		ans=$(haskell/p$x)
		end=$(date +%s)
		duration=$(echo "$end-$start" | bc)
		printf "Problem %3d: answer %12d " $(expr $x + 0) $ans 
		result=incorrect
		if ./checker.py $x $ans ; then 
			result=correct
			((correct=correct+1))
		fi
		printf "%10s %3ds\n" $result $duration
	fi
done


echo "$correct problems solved"
