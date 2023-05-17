// index.js

const express = require('express');
const { createServer } = require('http');
const { Server } = require('socket.io');

const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer);

app.set('view engine', 'ejs');
app.set('views', 'views');

// indico che i file statici si trovano nella cartella public
app.use(express.static('public'));

app.use(express.urlencoded({extended: false}));
app.use(express.json());

const admin = require("firebase-admin");

const serviceAccount = require("./serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const { getFirestore } = require('firebase-admin/firestore');
const db = getFirestore();
console.log(db);

/*const data = {
    name: 'Los Angeles';
    state: 'CA';
    country: 'USA';
}
*/
// Add a new document in collection 'cities' with ID 'LA'
//const res = db.collection('cities').doc('LA').set(data);

let todos = [
 {
    id: 1,
    text: "Play with Prof. Mazzone",
    done: false,
 },
 {
    id: 2,
    text: "Non distrarre il Prof. Mazzone",
    done: false,
 },
];

let nextId = 3

// get è un metodo http
//app.get('/', (req, res) => {
//    res.render('index', {
//        todos:todos,
//    });
//});

app.get('/', async (req, res) => {

    const todosRef = db.collection('todos');
    const snapshot = await todosRef.get();

    todos = [];
    snapshot.forEach((doc) => {
        console.log(doc);
        todos.push({...doc.data(), id : doc.id});
    });

    res.render('index', {
        author: 'Bocchetti Francesco',
        todos : todos,
    });
});

app.post('/mark-done', (req, res) => {
    const id = req.body.id;

    const todo = todos.find(todo => todo.id == id);
    todo.done = !todo.done;

    const todoRef = db.collection('todos').doc(todo.id);
    todoRef.update({ done: todos[todoIndex].done});
    //[todoIndex]

    res.redirect('/');
});

app.post('/clean', (req, res) => {
    todos = todos.filter(todo => todo.done == false)
    res.redirect('/');
});

app.post('/new_todo', (req, res) => {
    const text = req.body.text;

    const todo = {
        //id:nextId,
        text:text,
        done:false,
    }

    todos.push(todo);

    db.collection('todos').add(todo);

    res.redirect("/");
});

//Quando l'utente apre una connessione
io.on('connection', (socket) => {
    console.log('new connection here!');
    socket.emit('initial-data', {
        msg:'initial data here'
    });

    socket.on('hello', (data) => {
        console.log(data);
    });
});

//Invia ogni secondo a tutti i client un dato
setInterval(() => {
    io.emit('new-data', {
        value: Math.random()*10,
        timestamp: new Date(),
    })
}, 1000);

//app.listen(3000);
httpServer.listen(3000);