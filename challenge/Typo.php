#!/usr/bin/php
<?php

// Q: http://www.hacker.org/challenge/chal.php?id=144
// A: http://www.hacker.org/challenge/chal.php?answer=12%2C*&id=144&go=Submit

$expr = '$x = $y * 2245 + ($y * 2 - 7);';
$expr[12] = '*';
echo($expr);
echo("\n");

$y = 79;
eval($expr);
echo $x;
