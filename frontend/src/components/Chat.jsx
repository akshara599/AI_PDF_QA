import { useState, useEffect } from "react";
import axios from "axios";


function Chat() {

  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);


  // create user id
  const getUserId = () => {

    let id = localStorage.getItem("userId");

    if (!id) {

      id = crypto.randomUUID();

      localStorage.setItem(
        "userId",
        id
      );

    }

    return id;
  };


  const userId = getUserId();



  // load old chats
  useEffect(() => {


    const loadHistory = async()=>{

      try{

        const response = await axios.get(

          `${import.meta.env.VITE_BACKEND_URL}/history/${userId}`

        );


        const oldMessages=[];


        response.data.forEach(chat=>{


          oldMessages.push({

            type:"user",

            text:chat.question

          });


          oldMessages.push({

            type:"ai",

            text:chat.answer

          });


        });



        setMessages(oldMessages);


      }
      catch(error){

        console.log(error);

      }

    };


    loadHistory();


  },[]);





  const askQuestion = async()=>{


    if(!question) return;


    const userMessage={

      type:"user",

      text:question

    };


    setMessages(prev=>[

      ...prev,

      userMessage

    ]);


    setLoading(true);



    try{


        const response = await axios.post(
        `${import.meta.env.VITE_BACKEND_URL}/chat`,
        {
          question,
          user_id:userId
        }
        );

        console.log(response.data);

      const aiMessage = {
        type: "ai",
        text: response.data.answer || response.data.error
      };



      setMessages(prev=>[

        ...prev,

        aiMessage

      ]);



    }

    catch(error){

      console.log(error);

    }


    setQuestion("");

    setLoading(false);


  };




return (

<div>

<h2>💬 Ask PDF</h2>


<div className="chatWindow">


{

messages.map((msg,i)=>(


<div

key={i}

style={{

textAlign:
msg.type==="user"
?
"right"
:
"left",

margin:"10px 0"

}}

>


<div

style={{

display:"inline-block",

padding:"10px 15px",

borderRadius:"12px",

background:

msg.type==="user"

?

"#2563eb"

:

"#374151",

color:"white",

maxWidth:"80%"

}}

>


{msg.text}


</div>


</div>


))

}


</div>



<div className="chatBox">


<input

placeholder="Ask something..."

value={question}

onChange={(e)=>setQuestion(e.target.value)}

/>


<button onClick={askQuestion}>

{

loading

?

"Thinking..."

:

"Ask"

}

</button>


</div>


</div>


);


}


export default Chat;