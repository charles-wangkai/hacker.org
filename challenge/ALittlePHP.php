#!/usr/bin/php
<?php

// Q: http://www.hacker.org/challenge/chal.php?id=97
// A: http://www.hacker.org/challenge/chal.php?answer=18370&id=97&go=Submit

$x = 72311;
$y = 89525;
$z = '=';
eval("\$k$z\$x^\$y;");
echo $k;
