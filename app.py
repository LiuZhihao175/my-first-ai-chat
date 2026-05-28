from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        user_input = request.form["user_input"]

        chat_history.append({
            "sender": "You",
            "message": user_input,
            "time": datetime.now().strftime("%H:%M")
        })

        ai_reply = "Hello! I am your AI assistant."

        chat_history.append({
            "sender": "AI",
            "message": ai_reply,
            "time": datetime.now().strftime("%H:%M")
        })

    messages_html = ""

    for chat in chat_history:

        if chat["sender"] == "You":
            bubble_color = "#2B5278"
            align = "right"

        else:
            bubble_color = "#444654"
            align = "left"

        messages_html += f"""
        <div style="text-align:{align}; margin:10px 0;">

            <div style="
                display:inline-block;
                background:{bubble_color};
                padding:12px;
                border-radius:12px;
                max-width:60%;
                word-wrap:break-word;
                color:white;
            ">

                <div style="
                    display:flex;
                    align-items:center;
                    gap:8px;
                ">

                    <div style="
                        width:35px;
                        height:35px;
                        border-radius:50%;
                        background:white;
                        color:black;
                        text-align:center;
                        line-height:35px;
                        font-weight:bold;
                    ">
                        {"🤖" if chat["sender"] == "AI" else "👤"}
                    </div>

                    <b>{chat["sender"]}</b>

                </div>

                <br>

                {chat["message"]}

                <br><br>

                <div style="
                    font-size:12px;
                    color:#cccccc;
                ">
                    {chat["time"]}
                </div>

            </div>

        </div>
        """

    return render_template(
        "index.html",
        messages_html=messages_html
    )

if __name__ == "__main__":
    app.run(debug=True)