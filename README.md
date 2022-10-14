![poketroca_logo](https://user-images.githubusercontent.com/32853995/195741875-ca7b3e72-e1e8-4733-89be-1c725f679e3c.png)


<div align="center">
          
<a href="https://github.com/pedrohso7/PokeTroca/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/pedrohso7/PokeTroca"></a>
</div>
          
<p align="center">
  <a href="#-project">Project</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-technologies">Technologies</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-overview">Overview</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-poketroca-usecase-views">PokeTroca UseCase Views</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-usage">Usage</a>
</p>

## ✦ Project
<p align="justify">
PokeTroca is a distributed system of pokemon trade. This project gives to each registered user, ten random pokémons and you have to make the best team you can through good trades on the platform. With this project used three different communication between process for study reasons. 
          
The methods are:
</p>

<ul>
<li>Socket</li>
<li>RMI</li>
<li>Rest</li> 
</ul>

## ✦ Technologies
This project was made using the tecnologies below:
- [Python](https://www.python.org/)
- [Kivy](https://kivy.org/)
- [KivyMD](https://kivymd.readthedocs.io/en/1.1.1/)
- [Socket.io](https://python-socketio.readthedocs.io/en/latest/)
- [GRPCio](https://grpc.io/docs/languages/python/quickstart/)
- [SQlite](https://www.sqlite.org/index.html)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

## ✦ Overview
<p align="justify">
PokeTroca is composed by an architeture model on the physical layer as follows:
</p>


<p align="middle">
<img alt="PokeTroca physycal architeture" title="App" src="https://user-images.githubusercontent.com/32853995/195866908-820f8446-73c5-4993-abbc-5266d7c0436d.png" width="450"/>
</p>

<p align="justify">
In other words, our system follows the client-server approach, where the client was made in Python using Kivy and Kivymd to create beauty and friendly views and the server using Python and SQLite as database.
</p>


<p align="justify">
The logical layer (code part) of the server follows the Clean Architeture model:
</p>


<p align="middle">
<img alt="Server logic layer" title="App" src="https://user-images.githubusercontent.com/32853995/195869299-c56d34bc-15fc-4719-9dbc-ba12cadad163.png" width="450"/>
</p>

<p align="justify">
And about the client logical layer, it was made inspired on the traditional MVC architeture:
</p>

<p align="middle">
<img alt="Client logic layer" title="App" src="https://user-images.githubusercontent.com/32853995/195872089-eb6692f9-65de-4b10-ac89-6bce1ed79602.png" width="450"/>
</p>

<h4>What about the communication?</h4>
<p align="justify">
First of all, before make PokeTroca, we planned to use a simple route system created by us to simulate, even in Sockets or RMI methods, the request-response approch. In other words, we always send a route and params from client and we always expect this on the server side too and the reciprocal is true. Doing like this, we only had to be worry with the communication, the study object of this repository. 
</p>

<p align="justify">
This project implements, as we said, different kinds of comunication. At a first time, we used <b>Sockets</b> that works sending bytes from each process. So we decided to use an external representation that is a known way of data in both client and server, the JSON representation, to avoid any possibility of wrong behaviour.
</p>

<p align="justify">
The second communication method was RMI <b>(Remote Method Invocation)</br> that instead of make a requisition and wait for some response, the client execute a pré defined remote call procedure shared between client and server through .proto archives. The gRPC (Google Remote Procedure Call) framework helps us use this archives and call the remote methods.
</p>

<p align="justify">
Finally, the most used communication method, <b>Rest (Representational state transfer)</b> is implemented here with an API using Flask. In the client side was used a python library to use the http methods and make requests to server.
</p>

<p align="justify">
PokeTroca platform wants to show you there are so many ways to plane an application and we have to consider the context and the goals it wants to reach. Make sure, before starts a new project, to keep in mind the plane phase have the same importance as the code phase to boost your success accuracy.
</p>

## ✦ PokeTroca UseCase Views

<p align="middle">
<img alt="Login View" title="App" src="https://user-images.githubusercontent.com/32853995/195891274-eaa8adf4-e57d-472b-97f1-af2077087537.png" width="400"/>
<img alt="Register View" title="App" src="https://user-images.githubusercontent.com/32853995/195891331-8a53d8f6-5137-4b6a-9f53-a6a62c12131b.png" width="400"/>
<img alt="Home View" title="App" src="https://user-images.githubusercontent.com/32853995/195891428-c9d4f94f-eb7e-46a4-b2e5-c0ab04b01917.png" width="400"/>
<img alt="Inventory View" title="App" src="https://user-images.githubusercontent.com/32853995/195891477-88b8e008-3f1a-4775-837d-ae99d2791c17.png" width="400"/>
<img alt="Trade View" title="App" src="https://user-images.githubusercontent.com/32853995/195891560-5c554ea1-3074-4c70-a242-e054bee0fdcf.png" width="400"/>
<img alt="Barter's View" title="App" src="https://user-images.githubusercontent.com/32853995/195891625-7140f0c4-0511-405d-bdfb-be1436f0c0dd.png" width="400"/>
</p>

## ✦ Usage
<p align="justify">
First you have to create your .env file on root path following .env.example and then you're prepared to run and use the server.
</p>


<p align="justify">
Make sure you're on the root path and run the following command to get the dependencies using
</p>

```
npm install
```

<p align="justify">
Now you can run server:
</p>

```
node src/index.js
```

## ✦ Start to use

<p align="justify">
Clone this and use in your test.
</p>
