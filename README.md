## Chess Move Recommendation App

### Description
#### This repository contains all the code I used to build out and assess different chess recommendation functions. It also contains code for utilizing the recommendation functions in a Flask app where a custom chess configuration can be inputted. The app has been deployed to Heroku and can be found here: https://next-chess-move.herokuapp.com/
<br>

### Background
#### Chess is a popular game worldwide. One of the most popular chess websites, Chess.com, has over 60 million members. Therefore, I thought that an app which could provide chess move recommendations could have a potentially large user base. I used a minimax algorithm with alpha beta pruning as a baseline recommender, and a convolutional neural network model as a means to improve upon that recommendation.
<br>

### Data Used
#### Lichess Open Database August and September 2014 Data https://database.lichess.org/
<br>

### Tools Used
#### Python: Pandas, NumPy, Chess, Matplotlib, Keras, Tensorflow
#### Other: Flask, HTML, Javascript, CSS, Heroku
<br>

### File List
#### Main Folder
* __Chess App Presentation - Metis Final Project.pdf__: Slides from final presentation
* __Neural Net Data Set Creation.ipynb__: Cleans and filters data set that will be used in the neural network models
* __Expert Data Set Creation.ipynb__: Cleans and filters the data set that will be used for evaluation of the different recommenders
* __Convolutional Neural Network Models.ipynb__: Convolutional neural network models that were run
* __Evaluate Neural Network Models.ipynb__: Code to evaluate how well neural net predicted moves compared to moves in the expert data set
* __Create Histogram.ipynb__: Code to create histogram of the difference between the Elo ratings of the two players in each game
* __elo.svg__: Histogram of the difference between the Elo ratings of the two players in each game
#### chess_app Folder
* __chess_app.py__: Flask app code with the three recommenders
* __chess_minimax.py__: Functions to run minimax algorithm for a chessboard configuration
* __chess_neuralnet.py__: Functions to run neural net prediction for a chessboard configuration
* __chess_random.py__: Function that provides a random legal move for a chessboard configuration
* __evaluate_board.py__: Functions to assess chessboard configurations based on piece values 
* __Evaluate Random Moves and Minimax Algorithm.ipynb__: Code to evaluate how well random and minimax moves compared to moves in the expert data set
* __/models__: Folder of resulting convolutional neural net models
* __/static/css/chessboard-1.0.0.min.css__: CSS file adapted from chessboardjs documentation to change board colors
* __/static/chesspieces/wikipedia__: Folder containing piece images used for chessboard
* __/templates/chessboard.html__: HTML, Javascript, and CSS code for app template
<br>

### Evaluation and Conclusions
#### To evaluate how well each of my recommenders worked, I compared the recommended next moves to the actual next moves of chess players with Elo ratings of 2400. I found that my minimax algorithm performed about the same as choosing a move randomly, which was about 6% of moves matched. There are definitely improvements that I should make to the minimax algorithm that I used. The convolutional neural net model did perform better, with about 9% of moves matched. While better than the baseline recommender, there is still a lot of room for improvement. 
#### This project did provide only one recommendation per recommender for each chessboard configuration. In many cases, however, there may not be one single best move. There are many possible strategies for chess, especially early in the game. For simplicity, I focused on only providing one recommendation, but in certain cases providing multiple recommendations might be more appropriate. 
