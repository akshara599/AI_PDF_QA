import { useState } from "react";
import axios from "axios";

function Chat() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question) return;

    const userMessage = { type: "user", text: question };
    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    const response = await axios.post(
      `${import.meta.env.VITE_BACKEND_URL}/chat`,
      { question }
    );

    const aiMessage = { type: "ai", text: response.data.answer };

    setMessages((prev) => [...prev, aiMessage]);

    setQuestion("");
    setLoading(false);
  };

  return (
    <div>
      <h2>💬 Ask PDF</h2>

      {/* CHAT WINDOW */}
      <div className="chatWindow">
        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              textAlign: msg.type === "user" ? "right" : "left",
              margin: "10px 0",
            }}
          >
            <div
              style={{
                display: "inline-block",
                padding: "10px 15px",
                borderRadius: "12px",
                background: msg.type === "user" ? "#2563eb" : "#374151",
                color: "white",
                maxWidth: "80%",
              }}
            >
              {msg.text}
            </div>
          </div>
        ))}
      </div>

      {/* INPUT */}
      <div className="chatBox">
        <input
          placeholder="Ask something..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button onClick={askQuestion}>
          {loading ? "Thinking..." : "Ask"}
        </button>
      </div>
    </div>
  );
}

export default Chat;