![Desenho sem título](https://user-images.githubusercontent.com/32853995/195741505-7a70dda4-4f71-4286-8dd8-b8c67bd6400b.png)


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
  <a href="#-usage">Usage</a>
</p>

## ✦ Project
<p align="justify">
This is a test restful API wich have some authentication endpoints as:
          
-> Login
          
-> Register
          
-> Token Verification using JWT.
          
It was made to test my personal mobile projects, especially [this](https://github.com/pedrohso7/mobileCleanProjectTemplate).
</p>

## ✦ Technologies
This project was made using the tecnologies below:
- [NodeJs](https://nodejs.org/en/)
- [BCrypt](https://www.npmjs.com/package/bcrypt)
- [Express](https://expressjs.com/pt-br)
- [JWT](https://www.npmjs.com/package/jsonwebtoken)

## ✦ Overview
<p align="justify">
You can freely use this endpoints:
</p>

<h4>Login: /auth/login</h4>

<p align="justify">
A get method that receive email and password as query params and return a body with the user and token if user exists.
</p>

<img alt="Login" title="App" src="https://user-images.githubusercontent.com/32853995/195408304-a4ba173a-2c99-41a8-a512-95b42cb10b44.png" width="400"/>

<h4>Register: /auth/register</h4>


<p align="justify">A post method that receive email, password and name as body params and return a body with the user and token if user doesn't exist.</p>


<img alt="Register" title="App" src="https://user-images.githubusercontent.com/32853995/195408184-adb4c7b9-9f82-4f8f-a6ac-4f2ee712136d.png" width="400"/>

<h4>Token Verification using JWT: /auth/token</h4>

<p align="justify">
A get method that receive token and user id as query params and verify if the token is valid, returning a boolean.
</p>

<img alt="Token Verify" title="App" src="https://user-images.githubusercontent.com/32853995/195408096-4c51a1f5-df6b-4c74-b3df-03e2a057011a.png" width="400"/>

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
