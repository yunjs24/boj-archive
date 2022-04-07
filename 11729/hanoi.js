

const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');
input = Number(input[0]);

function solution(input) {
    let count = 0;
    let answer = [];

    const hanoi = (n, src, tmp, dst) => {
        if (!n) return;
        hanoi(n - 1, src, dst, tmp);
        answer.push([src, dst]);
        count += 1;
        hanoi(n - 1, tmp, src, dst);
    }

    hanoi(input, 1, 2, 3);
    console.log(count);
    return answer.map(i => i.join(" ")).join("\n");
}
console.log(solution(input));