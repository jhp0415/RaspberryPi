<?php
    $conn = mysqli_connect("13.125.251.95", "root", "cbnuroot123", "INFORM_DRONE_STATUS");
    mysqli_query($conn, "set names utf8");

    if(mysqli_connect_errno($conn))
        echo "데이터베이스 연결 실패: ".mysqli_connect_error();
    else
        echo "데이터베이스 연결 성공";

    $text = $_POST['_text'];
    echo $text;
    //mysqli_query($conn, "INSERT INTO DRONE_SPEAK VALUES('MI DRONE', '$text')");
    mysqli_query($conn, "UPDATE DRONE_SPEAK SET Broadcast = '$text' WHERE Name = 'MI DRONE'");

    //페이지 이동
    $prePage = $_SERVER['HTTP_REFERER'];
    header("location:".$prePage);
?>