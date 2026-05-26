from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
   api_key=""
)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        user_input = request.form["user_input"]

        chat_history.append({
            "sender": "You",
            "message": user_input
        })

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        ai_reply = response.choices[0].message.content

        chat_history.append({
            "sender": "AI",
            "message": ai_reply
        })

    messages_html = ""

    for chat in chat_history:

        if chat["sender"] == "You":
            bubble_color = "#DCF8C6"
            align = "right"

        else:
            bubble_color = "#F1F0F0"
            align = "left"

        messages_html += f"""
        <div style="text-align:{align}; margin:10px;">
            <div style="
                display:inline-block;
                background:{bubble_color};
                padding:12px;
                border-radius:12px;
                max-width:300px;
            ">
                <b>{chat["sender"]}</b><br>
                {chat["message"]}
            </div>
        </div>
        """

    return f"""
    <html>

    <head>
        <title>AI Chat Website</title>
    </head>

    <body style="
        font-family: Arial;
        background:#ECE5DD;
        padding:30px;
    ">

        <h1>My AI Chat Website</h1>

        <div style="
            background:white;
            padding:20px;
            border-radius:10px;
            min-height:400px;
        ">

            {messages_html}

        </div>

        <br>

        <form method="POST">

            <input 
                type="text"
                name="user_input"
                placeholder="Type your message..."
                style="
                    width:70%;
                    padding:12px;
                    border-radius:10px;
                    border:1px solid gray;
                "
            >

            <button
                type="submit"
                style="
                    padding:12px 20px;
                    border:none;
                    border-radius:10px;
                    background:#4CAF50;
                    color:white;
                "
            >
                Send
            </button>

        </form>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)