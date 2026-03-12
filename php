<?php

$ch = curl_init("https://coderbyte.com/api/challenges/json/age-counting");

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, 0);

$data = curl_exec($ch);
curl_close($ch);

$response = json_decode($data, true);

$count = 0;

// Extract all ages using regex
preg_match_all('/age=(\d+)/', $response["data"], $matches);

foreach ($matches[1] as $age) {
    if ((int)$age >= 50) {
        $count++;
    }
}

echo $count;
