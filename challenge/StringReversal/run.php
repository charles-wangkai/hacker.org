#!/usr/bin/php
<?php

// Q: http://www.hacker.org/challenge/chal.php?id=219
// A: (Submit the file content of program.txt)

require "../../shphp.phps";

$program = file_get_contents("program.txt");
$memory = file_get_contents("memory.txt");

echo (new SHVM) -> Run($program, $memory)["output"];
echo "\n\n";
echo $program;