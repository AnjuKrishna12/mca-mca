<?php
$a=6;
for($i=1;$i<=$a;$i++)
{
    $n[]=rand(0,100);
}
?>
<html>
    <head>
        <title>RANDOM GENERATOR</title>
    </head>
    <body>
        <p>
        <h4>random numbers generated are:-<br>
        </h4>
        <?php foreach ($n as $num): ?>
        <span><?php echo $num ?></span><br>
        <?php endforeach?>
        </p>
    </body>
</html>
