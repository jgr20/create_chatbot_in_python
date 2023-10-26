print("Hello, I'm a Chatbot \n")
User_Name =  input("What is your name? ")
print("How are you {0}. \n".format(User_Name))

User_Age = input("What is your age? ")
print("Oh, so your age is {0}. \n".format(User_Age))

User_Job = input("What is your job profile? ")
print("So you're a  {0}. \n".format(User_Job))

Hello, I'm a Chatbot 
What is your name? pythonscholar
How are you pythonscholar. 
What is your age? 26
Oh, so your age is 26. 
What is your job profile? python developer
So you're a python developer

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now, let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )

source code of the program

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot=ChatBot('Pythonscholar')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )
response = chatbot.get_response("How are you?")
print(response)

output of the program

I am doing well.


# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now, let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )

@app.route("/")
def index():
	render_template("index.html")
    
@app.route("/get", methods=["POST"])
def chatbot_response():
	msg = request.form["msg"]
	response = chatbot.get_response(msg)
	return response

from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Flask initialization
app = Flask(__name__)

chatbot=ChatBot('Pythonscholar')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Now let us train our bot with multiple corpus
trainer.train("chatterbot.corpus.english.greetings",
              "chatterbot.corpus.english.conversations" )

@app.route("/")
def index():
	
	return render_template("index.html")



@app.route("/get", methods=["GET","POST"])
def chatbot_response():
    msg = request.form["msg"]
    response = chatbot.get_response(msg)
    return str(response)

if __name__ == "__main__":
    app.run()

<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css')}}" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>

<body>
    <div class="row">
        <div class="col-md-10 mr-auto ml-auto">
    <h1>Pythonscholar ChatBot</h1>
    <form>
        <div id="chatbox">
            <div class="col-md-8 ml-auto mr-auto">
                <p class="botText"><span>Hi! I'm Pythonscholar.</span></p>
            </div>
        </div>
        <div id="userInput" class="row">
            <div class="col-md-10">
                <input id="text" type="text" name="msg" placeholder="Message" class="form-control">
                <button type="submit" id="send" class="btn btn-warning">Send</button>
            </div>
        </div>
    </form>
</div>
</div>

<script>
    $(document).ready(function() {
        $("form").on("submit", function(event) {
            var rawText = $("#text").val();
            var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
            $("#text").val("");
            $("#chatbox").append(userHtml);
            document.getElementById("userInput").scrollIntoView({
                block: "start",
                behavior: "smooth",
            });
            $.ajax({
                data: {
                    msg: rawText,
                },
                type: "POST",
                url: "/get",
            }).done(function(data) {
                var botHtml = '<p class="botText"><span>' + data + "</span></p>";
                $("#chatbox").append($.parseHTML(botHtml));
                document.getElementById("userInput").scrollIntoView({
                    block: "start",
                    behavior: "smooth",
                });
            });
            event.preventDefault();
        });
    });
</script>
</body>

</html>

body {
    font-family: Garamond;
}

h1 {
    color: black;
    margin-bottom: 0;
    margin-top: 0;
    text-align: center;
    font-size: 40px;
}

h3 {
    color: black;
    font-size: 20px;
    margin-top: 3px;
    text-align: center;
}
.row {
    display: flex;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px;
}

.ml-auto{
    margin-left:auto !important;
}
.mr-auto{
    margin-right:auto !important;
}

.col-md-10,.col-md-8,.col-md-4{
    position: relative;
    width: 100%;
    min-height: 1px;
    padding-right: 15px;
    padding-left: 15px;
}
.col-md-8{flex:0 0 66.666667%;max-width:66.666667%}
.col-md-4{flex:0 0 33.333333%;max-width:33.333333%}
.col-md-10{flex:0 0 83.333333%;max-width:83.333333%}

.form-control {
    background: no-repeat bottom,50% calc(100% - 1px);
    background-image: none, none;
    background-size: auto, auto;
    background-size: 0 100%,100% 100%;
    border: 0;
    height: 36px;
    transition: background 0s ease-out;
    padding-left: 0;
    padding-right: 0;
    border-radius: 0;
    font-size: 14px;
}
.form-control {
    display: block;
    width: 100%;
    padding: .4375rem 0;
    padding-right: 0px;
    padding-left: 0px;
    font-size: 1rem;
    line-height: 1.5;
    color: #495057;
    border:none;
    background-color: transparent;
    background-clip: padding-box;
    border-bottom: 1px solid #d2d2d2;
    box-shadow: none;
    transition: border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}
.btn {
    float: left;
    text-align: center;
    white-space: nowrap;
    vertical-align: middle;
    user-select: none;
    border: 1px solid transparent;
    padding: .46875rem 1rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: .25rem;
    transition: color .15s ease-in-out,background-color .15s ease-in-out,border-color .15s ease-in-out,box-shadow .15s ease-in-out;
}
.btn-warning {
    color: #fff;
    background-color: #f08f00;
    border-color: #c27400;
}
.btn.btn-warning:active, .btn.btn-warning:focus, .btn.btn-warning:hover {
    box-shadow: 0 14px 26px -12px rgba(255,152,0,.42),0 4px 23px 0 rgba(0,0,0,.12),0 8px 10px -5px rgba(255,152,0,.2);
}

button, input, optgroup, select, textarea {
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
    overflow:visible;
}
#chatbox {
    background-color: cyan;
    margin-left: auto;
    margin-right: auto;
    width: 80%;
    min-height: 70px;
    margin-top: 60px;
}

#userInput {
    margin-left: auto;
    margin-right: auto;
    width: 40%;
    margin-top: 60px;
}

#textInput {
    width: 87%;
    border: none;
    border-bottom: 3px solid #009688;
    font-family: monospace;
    font-size: 17px;
}

#buttonInput {
    padding: 3px;
    font-family: monospace;
    font-size: 17px;
}

.userText {
    color: white;
    font-family: monospace;
    font-size: 17px;
    text-align: right !important;
    line-height: 30px;
    margin: 5px;
}

.userText span {
    background-color: #009688;
    padding: 10px;
    border-radius: 2px;
}

.botText {
    color: white;
    font-family: monospace;
    font-size: 17px;
    text-align: left;
    line-height: 30px;
    margin: 5px;
}

.botText span {
    background-color: #ef5350;
    padding: 10px;
    border-radius: 2px;
}

#tidbit {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 300px;
}

    
    
