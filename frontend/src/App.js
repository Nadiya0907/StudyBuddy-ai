import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [topic, setTopic] = useState("");
  const [answer, setAnswer] = useState("");

  const [notes, setNotes] = useState("");
  const [summary, setSummary] = useState("");
  const [quizTopic, setQuizTopic] = useState("");
  const [quiz, setQuiz] = useState("");
  const [quizData, setQuizData] = useState([]);
  const [answers, setAnswers] = useState({});
  const [score, setScore] = useState(null);
  const [flashcardTopic, setFlashcardTopic] = useState("");
  const [flashcards, setFlashcards] = useState("");
  const explainTopic = async () => {

    const response = await axios.post(
      "http://127.0.0.1:5000/explain",
      {
        topic: topic
      }
    );

    setAnswer(response.data.answer);
  };
  const summarizeNotes = async () => {
  try {
    const response = await axios.post(
      "http://127.0.0.1:5000/summarize",
      {
        notes: notes
      }
    );
    console.log("FULL RESPONSE:", response.data);


    setSummary(response.data.summary);

  } catch (error) {
    console.error(error);
    setSummary("Error generating summary");
  }
};
const generateQuiz = () => {

  const sampleQuiz = [
    {
      question: "What is Binary Search?",
      options: [
        "Sorting Algorithm",
        "Searching Algorithm",
        "Graph Algorithm",
        "Database"
      ],
      answer: "Searching Algorithm"
    },

    {
      question: "Time Complexity of Binary Search?",
      options: [
        "O(n)",
        "O(log n)",
        "O(n²)",
        "O(1)"
      ],
      answer: "O(log n)"
    }
  ];

  setQuizData(sampleQuiz);
  setScore(null);
};

const handleOptionChange = (questionIndex, option) => {
  setAnswers({
    ...answers,
    [questionIndex]: option
  });
};
const submitQuiz = () => {

  let total = 0;

  quizData.forEach((q, index) => {

    if (answers[index] === q.answer) {
      total++;
    }

  });

  setScore(total);
};
const generateFlashcards = async () => {

  try {

    const response = await axios.post(
      "http://127.0.0.1:5000/flashcards",
      {
        topic: flashcardTopic
      }
    );

    setFlashcards(response.data.flashcards);

  } catch (error) {

    console.error(error);

    setFlashcards(
      "Error generating flashcards"
    );

  }

};
  return (
    <div style={{ padding: "20px" }}>

      <h1>AI Study Buddy</h1>

      <input
        type="text"
        placeholder="Enter Topic"
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
      />

      <button onClick={explainTopic}>
        Explain
      </button>

      <hr />

      <h3>Explanation:</h3>

<div>

  {quizData.map((q, index) => (

    <div
      key={index}
      className="result-box"
      style={{ marginBottom: "20px" }}
    >

      <h4>
        Q{index + 1}. {q.question}
      </h4>

      {q.options.map((option, i) => (

        <div key={i}>

          <input
            type="radio"
            name={`question-${index}`}
            value={option}
            onChange={() =>
              handleOptionChange(index, option)
            }
          />

          {option}

        </div>

      ))}

    </div>

  ))}

  {quizData.length > 0 && (

    <button onClick={submitQuiz}>
      Submit Quiz
    </button>

  )}

  {score !== null && (

    <h2>
      🎉 Score: {score}/{quizData.length}
    </h2>

  )}

</div>
      

      <hr />

<h2>Notes Summarizer</h2>

<textarea
  rows="8"
  cols="60"
  placeholder="Paste your notes here..."
  value={notes}
  onChange={(e) => setNotes(e.target.value)}
></textarea>

<br /><br />

<button onClick={summarizeNotes}>
  Summarize Notes
</button>

<h3>Summary:</h3>


<div className="result-box">
  {summary}
</div>
<hr />

<h2>🎯 Quiz Generator</h2>


<input
  type="text"
  placeholder="Enter Topic for Quiz"
  value={quizTopic}
  onChange={(e) => {
    console.log("Typing:", e.target.value);
    setQuizTopic(e.target.value);
  }}
/>

<p>Typed Text: {quizTopic}</p>
<br /><br />

<button onClick={generateQuiz}>
  Generate Quiz
</button>
<hr />

<h2>📚 Flashcard Generator</h2>

<input
  type="text"
  placeholder="Enter Topic"
  value={flashcardTopic}
  onChange={(e) =>
    setFlashcardTopic(e.target.value)
  }
/>

<br /><br />

<button onClick={generateFlashcards}>
  Generate Flashcards
</button>

<h3>Flashcards:</h3>

<div className="result-box">
  {flashcards}
</div>


<h3>Quiz:</h3>

<div>

  {quizData.map((q, index) => (

    <div
      key={index}
      className="result-box"
      style={{ marginBottom: "20px" }}
    >

      <h4>Q{index + 1}. {q.question}</h4>

      {q.options.map((option, i) => (

        <div key={i}>

          <input
            type="radio"
            name={`question-${index}`}
            value={option}
            onChange={() =>
              handleOptionChange(index, option)
            }
          />

          {option}

        </div>

      ))}

    </div>

  ))}

  {quizData.length > 0 && (
    <button onClick={submitQuiz}>
      Submit Quiz
    </button>
  )}

  {score !== null && (
    <h2>
      🎉 Score: {score}/{quizData.length}
    </h2>
  )}

</div>

    </div>
  );

}
export default App;
