<?php

function add($a, $b){
  // Hint: Type return $a * $b; below
  return $a * $b;
}

$handle = fopen("php://stdin", "r");
$_a = fgets($handle);
$_b = fgets($handle);
$ret = add((int)$_a, (int)$_b);
print($ret);
fclose($handle);
?>
