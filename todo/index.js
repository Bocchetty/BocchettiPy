// index.js

const express = require('express');
const app = express();

app.set('view engine', 'ejs');
app.set('views', 'views');

// indico che i file statici si trovano nella cartella public
app.use(express.static('public'));

app.use(express.urlencoded({extended: false}));
app.use(express.json());

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

// get è un metodo http
app.get('/', (req, res) => {
    res.render('index', {
        todos:todos,
    });
});

app.post('/mark-done', (req, res) => {
    const id = req.body.id;

    const todo = todos.find(todo => todo.id == id);
    todo.done = !todo.done;

    res.redirect('/');
});

app.post('/clean', (req, res) => {
    todos = todos.filter(todo => todo.done==false)
})

app.post('/add_todo', (req, res) => {
    const todo= {
        id: nextid,
        text:req.body.text,
        done:false
    }
    todos++
    todos.push(todo);
    res.redirect("/")
})

app.listen(3000);