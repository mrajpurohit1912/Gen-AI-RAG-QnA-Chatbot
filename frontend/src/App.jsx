import { useState, useEffect } from 'react'
import './App.css'
import SearchBar from './components/SearchBar/SearchBar'
import Button from './components/Button/Button'

const API_URL = import.meta.env.VITE_API_URL;

function App() {
  const [theme, setTheme] = useState("light")
  const [question,setQuestion] = useState("")
  const [answer,setAnswer] = useState("")

  useEffect(() => {
    document.body.className = theme
  }, [theme])


  const handleSubmit = async () => {
    if (!question.trim()) return alert("Please enter a question")

    try{
      // const response = await fetch("http://127.0.0.1:5000/ask", {
        const response = await fetch(`${API_URL}/ask`, {
        method: "POST",
          headers: {
            "Content-Type": "application/json",
            
          },
          body: JSON.stringify({ question })
        })

      const data = await response.json();
      setAnswer(data.answer)
      console.log("Backend Response: ",data.answer)
      //alert("Response: " + JSON.stringify(data))
      
    }catch(error){
      console.error("Error: ",error)
      setAnswer("Error Fetcing response")
    }
  } 

  return (
    <>
      <header>
        <h1>Welcome to EdTech Platform</h1>
      </header>
      <div className='app-container'>
        <SearchBar value={question} onChange={setQuestion}/>
        <Button text="Submit" onClick={handleSubmit}/>
        
        {answer && (
          <div className='answer-container'>
            <h3 style={{ color: 'white' }}> Answer: </h3>
            <p> {answer}</p>
          </div>
        )}
        
      </div>
    </>
  )
}

export default App
