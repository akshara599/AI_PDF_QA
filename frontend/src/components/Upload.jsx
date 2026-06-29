import axios from "axios";
import {useState} from "react";


function Upload(){

const [status,setStatus]=useState("");


const uploadPDF = async(e)=>{


const selectedFiles = Array.from(e.target.files);


if(selectedFiles.length === 0){
    return;
}


const formData = new FormData();


selectedFiles.forEach((file)=>{

    formData.append(
        "files",
        file
    );

});


setStatus("Uploading PDFs...");


try{


const response = await axios.post(

`${import.meta.env.VITE_BACKEND_URL}/upload`,

formData,

{
headers:{
"Content-Type":"multipart/form-data"
}
}

);


console.log(response.data);


setStatus(
`✅ ${selectedFiles.length} PDFs Ready for questions`
);


}

catch(error){

console.log(error.response?.data || error.message);

setStatus("❌ Upload failed");

}



}



return(

<div>


<h2>
📄 Upload PDFs
</h2>


<input

type="file"

multiple

accept=".pdf"

onChange={uploadPDF}

/>


<p>{status}</p>


</div>

)


}


export default Upload;