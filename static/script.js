async function generateSchedule(){

    let year=document.getElementById("year").value;

    let month=document.getElementById("month").value;

    let absent=document.getElementById("absent").value;

    absent=absent.split(",")
                 .filter(x=>x!="")
                 .map(Number);

    let response=await fetch("/schedule",{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            year:year,

            month:month,

            absent:absent

        })

    });

    let data=await response.json();

    let body=document.getElementById("tableBody");

    body.innerHTML="";

    data.forEach(row=>{

        body.innerHTML+=`

        <tr>

        <td>${row.date}</td>

        <td>${row.day}</td>

        <td>${row.batch}</td>

        <td>${row.status}</td>

        </tr>

        `;

    });

}