import "./App.css";
import Upload from "./components/Upload";
import Chat from "./components/Chat";


function App() {
  return (
    <div className="container">
      <h1>🤖 AI PDF Q&A</h1>
      <p className="subtitle">
        Upload your PDF and ask anything
      </p>

      <div className="card">
        <Upload />
      </div>

      <div className="card">
        <Chat />
      </div>
    </div>
  );
}
export default App;