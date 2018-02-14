<!DOCTYPE html>
<html>
<head>
    <title>jquery demo!</title>
    <script type="text/javascript" src='http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'></script>
    <script type="text/javascript">





$(document).ready(function)(){
    alert('you are now working with jquery');

    $('a').click(function(){
        alert('you are now leaving the page');
    })
}
