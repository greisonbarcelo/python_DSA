SET logic to rock > scissors, scissors > paper, paper > rock

GET name

SET user_points and computer_points to zero
SET round to zero
SET max round to 3
SET user_hand and computer_hand to none
SET winner to none


LOOP 3 times/round at the beginning of the game

GET user_hand
GET random computer_hand

COMPARE user_hand to computer_hand using logic

UPDATE user_points/computer to winner of the round

UPDATE round + 1

COMPARE if round == 3
IF round == 3
COMPARE user_points to computer_points
DECLARE winner on who got more points
IF user_points = computer_points = TIE

PROMPT if you want to play again Y/N
IF yes > call the game function
ELSE no > SET NAME = ''
