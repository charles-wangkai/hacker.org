#!/usr/bin/php
<?php

// Q: http://www.hacker.org/challenge/chal.php?id=245
// A: http://www.hacker.org/challenge/chal.php?answer=10%2C0&id=245&go=Submit

$expr = '$x = $y * 2245 + ($y * 2 - 7);';
$expr[10] = '0';
echo $expr;
echo "\n";

$y = 79;
eval($expr);
echo $x;
