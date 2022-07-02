const process = require("process");

const questions = [
    "O que você aprendeu?",
    "O que te aborreceu?",
    "Como melhorar isso?",
    "O que você mais gostou de fazer?",
    "Quantas pessoas você ajudou?"
];

const answers = [];

ask = (index = 0) => {
    return process.stdout.write("\n\n" + questions[index] + "\n >>> ");
}

process.stdout.write("Olá Leandro, vamos repassar o seu dia de hoje!");
ask();

process.stdin.on("data", data => {
    answers.push(data);
    if(answers.length < questions.length){
        ask(answers.length);
    }
    else 
        process.exit()
})

process.on("exit", () => {
    process.stdout.write(`
    ###################################
    Mural do dia
    1- ${questions[0]}
    ${answers[0]}

    2 - ${questions[1]}
    ${answers[1]}

    3 - ${questions[2]}
    ${answers[2]}

    4 - ${questions[3]}
    ${answers[3]}

    5 - ${questions[4]}
    ${answers[4]}

    Ate amanha
    ###################################
    `)
})