// 문자열 출력하기

// 문제 설명
// 문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.

// 제한사항
// 1 ≤ str의 길이 ≤ 1,000,000
// str에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.

const readline = require('readline'); // 입력을 위한 모듈
const rl = readline.createInterface({ //`readline` 모듈을 이용해 인터페이스 생성
    input: process.stdin,  // input(들어오는 값)을 받기 위한 인터페이스
    output: process.stdout // output(나가는 값)을 받기 위한 인터페이스
});

let input = []; // 입력 값을 저장할 배열

rl.on('line', function (line) {  // 입력을 받아와서 input에 저장
    input = [line]; // 입력받은 값을 input 배열에 저장
}).on('close',function(){ // 입력받는 것을 종료하면
    str = input[0]; // input 배열의 첫번째 값을 str에 저장
    console.log(str); // str 출력
});