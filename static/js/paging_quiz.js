"use strict"
var questions = [
  {
    question: "Which of the following page replacement algorithms suffers from Belady’s Anomaly?",
    choices: ["Optimal replacement", "LRU", "FIFO", "Both optimal replacement and FIFO"],
    correctAnswer: 2
  },
  {
    question: "A process refers to 5 pages, A, B, C, D, E in the order : A, B, C, D, A, B, E, A, B, C, D, E. If the page replacement algorithm is FIFO, the number of page transfers with an empty internal store of 3 frames is?",
    choices: ["8", "10", "9", "7"],
    correctAnswer: 2
  },
  {
    question: "A FIFO replacement algorithm associates with each page the _______",
    choices: ["time it was brought into memory", "size of the page in memory", "page after and before it", "all of the mentioned"],
    correctAnswer: 0
  },
  {
    question: "LRU page – replacement algorithm associates with each page the ______",
    choices: ["time it was brought into memory", "the time of that page’s last use", "page after and before it", "all of the mentioned"],
    correctAnswer: 3
  },
  {
    question: "What are the two methods of the LRU page replacement policy that can be implemented in hardware?",
    choices: ["Counters", "RAM & Registers", "Stack & Counters", "Registers"],
    correctAnswer: 2
  }
];


/* MODEL
  - functions that deal with the data
*/
function Question(num) {
  this.num = num;
  this.question = questions[num].question;
  this.choices = questions[num].choices;
  this.correctAnswer = questions[num].correctAnswer;
}
Question.prototype.getQuestion = function(num) {
  return questions[num];
};

/* CONTROLLER
  - logic that coordinates between model and view
*/
function Quiz(questions) {
  this.questions = questions;

  this.userAnswers = [];
}
Quiz.prototype.startQuiz = function(game) {
  this.num = 0;
  this.score = 0;

  var currentQuestion = new Question(this.num);
  game.showQuestion(currentQuestion.getQuestion(this.num));
};
Quiz.prototype.nextQuestion = function(choice) {
  var currentQuestion = new Question(this.num);
  if (this.checkAnswer(choice, currentQuestion.getQuestion(this.num))) {
    quiz.score++;
  }
  if (this.num + 1 >= questions.length) {
    this.endQuiz(this.score, this.userAnswers);
  }
  else {
    this.num++;
    var currentQuestion = new Question(this.num);
    game.showQuestion(currentQuestion.getQuestion(this.num));
  }
};
Quiz.prototype.checkAnswer = function(choice, currentQuestion) {
  this.currentQuestion = currentQuestion;
  this.choice = choice;
  this.userAnswers.push(this.choice);
  return currentQuestion.correctAnswer == choice;
};
Quiz.prototype.showAnswers = function(userAnswers) {
  var answers = "<h3>Answers (incorrect in red): </h3><ol>";
  var userAnswers = this.userAnswers;

  this.questions.forEach(function(question, index) {
    // if the correct answer doesn't match the user's answer, change styling
    if (question.correctAnswer != userAnswers[index]) {
      answers += "<li><p>" + question.question + "</p><p><b class='red'>" + question.choices[question.correctAnswer] + "</b></p></li>";
    }
    else {
      answers += "<li><p>" + question.question + "</p><p>" + question.choices[question.correctAnswer] + "</p></li>";
    }
    // if it's the last question, don't add a comma to the string
    if (index === questions.length - 1) {
      answers += "</ol>";
    }
  });
  return answers;
};
Quiz.prototype.endQuiz = function(score, userAnswers) {
  this.score = score;
  this.userAnswers = userAnswers;
  this.answers = this.showAnswers(this.userAnswers);
  game.resetQuiz(this.score, this.answers);
};


/* VIEW
  - displays data to user and handles click events
*/
function Game(quiz) {
  this.quiz = quiz;
}
$("#next").click(function() {
  var choice = $(".choices input[name=choice]:checked").val()
  if (choice == undefined) {
    $("#question-group").effect("shake");
    return;
  }
  quiz.nextQuestion(choice);
});
$("#reset").click(function() {
  $("#next").toggleClass("hide");
  $("#reset").toggleClass("hide");
  $("#answers").empty();

  $("#score").empty();
  game.newGame();
});
$("#show-answers").click(function() {
  $(this).parent().toggleClass("hide");
});
Game.prototype.showQuestion = function(currentQuestion) {
  this.currentQuestion = currentQuestion;
  var radios = "";

  $("#question").text(this.currentQuestion.question);
  for (var i = 0; i < this.currentQuestion.choices.length; i++) {
    radios += "<label><input type='radio' class='choice' name='choice' value='" + i + "'>" + this.currentQuestion.choices[i] + "</label>";
  }
  $(".choices").html(radios);
};
Game.prototype.resetQuiz = function(score, answers) {
  this.score = score;

  //$("#question").text("Game over!");
  $("#score").text("You scored " + this.score + " points!");
  $("#answers").html(answers).toggleClass("hide");

  $(".choices").empty();
  $("#next").toggleClass("hide");
  $("#reset").toggleClass("hide");
};
Game.prototype.newGame = function() {
  this.quiz = new Quiz(questions);
  game = new Game(this.quiz);
  quiz.startQuiz(game);
};

var quiz = new Quiz(questions);
var game = new Game(quiz);
quiz.startQuiz(game);