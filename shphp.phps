<?php
class SHVM {
  public $MAX_CYCLES = 10000;
  private $movin = array(array(1, 0), array(0, -1), array(-1, 0), array(0, 1));
  //  public $MEM_HEIGHT = 8;
  public $MEM_HEIGHT = 128;
  public $MEM_WIDTH = 1024;
  public $MAX_THREADS = 32;
  private $timeToQuit = false;
  
  public $Memory = array();
  public $Threads = array();
  public $Code = array();
  public $user_input = array();
  public $trace = false;
  private $t = NULL;
  public $cycle_count = 0;
			 
  private function InitStuff() {
    $this->timeToQuit = false;
    $this->Code = array();
    $this->Memory = array();
    for ($i = 0; $i < $this->MEM_HEIGHT; $i++) {
      $this->Memory[$i] = array_fill(0, $this->MEM_WIDTH, 0);
	 }
    $this->Threads = array();
    $this->t = array();
    $this->t['pcX'] = 0; $this->t['pcY'] = 0;
    $this->t['mX'] = -1; $this->t['mY'] = 0;
    $this->t['dir'] = 0;
    $this->t['cs'] = array();
    $this->Threads[0] = $this->t;
  }
  
  private function Push($v) {
    if ($v > 2147483647 || $v < -2147483648) throw new Exception("integer overflow: '$v'");
    $this->t['mX'] += 1;
    $this->Memory[$this->t['mY']][$this->t['mX']] = $v;
  }
  
    private function Pop() {
      if ($this->t['mX'] < 0) throw new Exception("stack underflow");
      $v = $this->Memory[$this->t['mY']][$this->t['mX']];
      $this->t['mX'] -= 1;
      return $v;
    }

   private function MoveOneStep() {
     $this->t['pcX'] += $this->movin[$this->t['dir']][0];
     $this->t['pcY'] += $this->movin[$this->t['dir']][1];
   }
  
  function Run($code, $mem_init, $traceIt = false) {
    $this->InitStuff();

    $output = "";
    $message = "";
    $result = 0;
    
    $lines = preg_split('/[\n\r]+/', $code);
	 //	 print_r($lines);
    for ($y = 0; $y < count($lines); $y++) {
		$this->Code[$y] = array();
      for ($x = 0; $x < strlen($lines[$y]); $x++) {
		  $c = $lines[$y][$x];
		  $this->Code[$y][$x] = $c;
		  if ($c == '%') {
			 $this->Threads[0]['pcX'] = $x;
			 $this->Threads[0]['pcY'] = $y;
		  }
      }
    }

    // initialize the memory
    $mem_init_cells = explode(",", $mem_init);
    for ($i=0; $i<count($mem_init_cells); $i++) {
      $this->user_input[$i] = (int)trim($mem_init_cells[$i]);
    }
	 $this->user_input = array_reverse($this->user_input);
    
    // run loop
    try {
      while (!$this->timeToQuit) {
        // check that we don't exceed the max
        if ($this->cycle_count++ > $this->MAX_CYCLES) throw new Exception('too many cycles: ' . $this->cycle_count);
		  for ($tindex = 0; $tindex < count($this->Threads); $tindex++) {
			 $this->t =& $this->Threads[$tindex];
			 // some convenience vars
			 $t =& $this->t;
			 $pcX =& $t['pcX']; $pcY =& $t['pcY'];
			 $mX =& $t['mX']; $mY =& $t['mY'];
			 $mem =& $this->Memory;
			 $dir =& $t['dir'];
			 //			 print_r($this->t);
			 if ($pcY < 0 || $pcX < 0) throw new Exception('out of code bounds');
			 
			 if (!isset($this->Code[$pcY])) {
				$s = 'undefined code vert: ' . $mX.",xxxxxx". $pcX;
				throw new Exception($s);
			 }
			 if (!isset($this->Code[$pcY][$pcX])) throw new Exception('undefined code: ' . $pcY.",". $pcX);
			 $instruction = $this->Code[$t['pcY']][$pcX];
			 $ox = $pcX; $oy = $pcY;

			 if ($traceIt) echo "[Thread $tindex] <b>$instruction</b> @$ox,$oy [".implode(',', array_slice($this->Memory[$mY], 0, $mX + 1) )."]\n<br>";
			 //			 if ($traceIt) echo "[Thread $tindex] <b>$instruction</b> @$ox,$oy [".implode(',', array_splice(0, $this->Memory[$this->t['mY']], $mX + 1))."]\n<br>";

			 // instruction dispatch
			 switch ($instruction) {
			 case ' ': break;
			 case '0': $this->Push(0); break;
			 case '1': $this->Push(1); break;
			 case '2': $this->Push(2); break;
			 case '3': $this->Push(3); break;
			 case '4': $this->Push(4); break;
			 case '5': $this->Push(5); break;
			 case '6': $this->Push(6); break;
			 case '7': $this->Push(7); break;
			 case '8': $this->Push(8); break;
			 case '9': $this->Push(9); break;
			 case '+': $this->Push($this->Pop()+$this->Pop()); break;

			 case '-': $a = $this->Pop(); $b = $this->Pop(); $this->Push($b-$a); break;
			 case '*': $this->Push($this->Pop()*$this->Pop()); break;
			 case 'd': $a = $this->Pop(); $b = $this->Pop(); $this->Push(floor($b/$a)); break;
			 case '\\': $dir = ($dir ^ 3); break;
			 case '/': $dir = ($dir ^ 1); break;
			 case 'p': $output .= $this->Pop(); break;
			 case 'P': $output .= chr($this->Pop()&0x7F); break;
			 case ':': $a = $this->Pop(); $b = $this->Pop(); if ($b<$a) $dir = ($dir + 1) % 4; else if ($b > $a) $dir = ($dir + 3) % 4; break;
				//	case ':': $a = $this->Pop(); $b = $this->Pop(); $this->Push( ($b<$a)?-1:(($b==$a)?0:1)); break;
			 case ',': if (count($this->user_input) > 0) $this->Push(array_pop($this->user_input)); else $this->Push(0); break;
			 case 's': $this->MoveOneStep(); break;
			 case '?': $a = $this->Pop(); if ($a == 0) $this->MoveOneStep(); break;
			 case '@':
				array_push($this->t['cs'], array($pcX, $pcY, $dir));
				break;
			 case '$':
				if (count($this->t['cs']) == 0) throw new Exception("call stack underflow");
				$c = array_pop($this->t['cs']);
				$pcX = $c[0]; $pcY = $c[1]; $dir = $c[2];
				$this->MoveOneStep();
				break;
			 case '<':
				$x = $this->Pop(); $y = $this->Pop();
				if ($x < 0 || $y < 0) throw new Exception('memory read access violation @'.$x.",".$y);
				if ($y >= count($this->Memory))
				  $this->Push(0);
				else {
				  $this->Push($this->Memory[$y][$x]);
				}
				break;
			 case '>':
				$x = $this->Pop(); $y = $this->Pop();
				if ($x < 0 || $y < 0) throw new Exception('memory read access violation @'.$x.",".$y);
				$val = $this->Pop();
				$this->Memory[$y][$x] = $val;
				//	  print_r($mem);
				break;
			 case '[': $i = $this->Pop(); $mX -= $i; break; 
			 case ']': $i = $this->Pop(); $mX += $i; break; 
			 case '{': $mY--; if ($mY < 0) throw new Exception("mem cannot go neg"); break;
			 case '}': $mY++; if ($mY == $this->MEM_HEIGHT) throw new Exception("mem too big"); break; 
			 case 'x': $a = $this->Pop(); $this->Push($a); $this->Push($a); break; 
			 case '^': $a = $this->Pop(); 
				if ($a < 0 || $mX < $a) throw new Exception("out of mem bounds: $a, $mX");
				$this->Push($this->Memory[$mY][$mX - $a]); break;
			 case 'v':
				$a = $this->Pop(); 
				if ($a < 0 || $mX < $a) throw new Exception("out of mem bounds: $a, $mX");
				$v = array_splice($this->Memory[$mY], $mX - $a, 1);
				array_splice($this->Memory[$mY], $mX, 0, $v[0]); // insert value at mem
				break;
			 case 'g':
				$x = $this->Pop(); $y = $this->Pop();
				$v = ord($this->Code[$y][$x]);
				$this->Push($v);
				break;
			 case 'w':
				$x = $this->Pop(); $y = $this->Pop(); $c = $this->Pop();
				$this->Code[$y][$x] = chr($c & 0x7f);
				break;
			 case '&':
				if (count($this->Threads) == $this->MAX_THREADS) throw new Exception("max threads exceeded: " . $this->MAX_THREADS);
				$nt = array();
				$nt['pcX'] = $pcX; $nt['pcY'] = $pcY;
				$nt['mX'] = $mX; $nt['mY'] = $mY;
				$nt['dir'] = $dir;
				$nt['cs'] = array();
				$nt['pcX'] += $this->movin[$dir][0];
				$nt['pcY'] += $this->movin[$dir][1];
				array_push($this->Threads, $nt);
				$this->MoveOneStep();
				break;
			 case '!': $this->timeToQuit = true; break;
			 default: break;
			 }
			 
			 $this->MoveOneStep();
		  }
      }
    } catch (Exception $e) {
      $message = $e->getMessage() . " (PC=" . ($this->t['pcX'] . ", " . $this->t['pcY']) . ")";
      $result = -1;
      //      print_r($this);
    }
    
    return array("result" => $result, "message" => $message, "cycles" => $this->cycle_count, "output" => $output);
  }
}
?>
