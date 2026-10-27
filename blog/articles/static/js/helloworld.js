var groupmates = [
    {"name": "Сергей", "surname": "Уткин", "group": "БСТ2354", "marks": [5, 4, 5]},
    {"name": "Алина", "surname": "Бестаева", "group": "БСТ2354", "marks": [4, 4, 3]},
    {"name": "Давид", "surname": "Кесаев", "group": "БВТ2301", "marks": [5, 5, 5]},
    {"name": "Мадина", "surname": "Дзуцева", "group": "БСТ2354", "marks": [3, 4, 3]},
    {"name": "Тимур", "surname": "Цаллаев", "group": "БАП2302", "marks": [4, 5, 4]},
    {"name": "Залина", "surname": "Хадонова", "group": "БВТ2301", "marks": [3, 3, 4]}
];

console.log(groupmates);

var rpad = function(str, length) {
    // js не поддерживает добавление нужного количества символов
    // справа от строки, т.е. аналога ljust из Python здесь нет
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки
    return str; // когда все пробелы добавлены, возвратить строку
};

var printStudents = function(students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    // был выведен заголовок таблицы
    for (var i = 0; i <= students.length - 1; i++) {
        // в цикле выводится каждый экземпляр студента
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};

// средний балл студента
var average = function(marks) {
    var sum = 0;
    for (var i = 0; i < marks.length; i++) sum += marks[i];
    return sum / marks.length;
};

// фильтрация студентов по группе
var filterByGroup = function(students, group) {
    var result = [];
    for (var i = 0; i < students.length; i++) {
        if (students[i]['group'].toUpperCase() == group.trim().toUpperCase()) {
            result.push(students[i]);
        }
    }
    return result;
};

// фильтрация студентов по среднему баллу (выше заданного)
var filterByMark = function(students, minAvg) {
    var result = [];
    for (var i = 0; i < students.length; i++) {
        if (average(students[i]['marks']) > minAvg) {
            result.push(students[i]);
        }
    }
    return result;
};

console.log("Все студенты:");
printStudents(groupmates);

var group = prompt("Введите группу для фильтрации (например, БСТ2354):", "БСТ2354");
if (group !== null) {
    console.log("Студенты группы " + group + ":");
    printStudents(filterByGroup(groupmates, group));
}

var mark = prompt("Введите средний балл для фильтрации:", "4");
if (mark !== null) {
    mark = parseFloat(mark.replace(",", "."));
    console.log("Студенты со средним баллом выше " + mark + ":");
    printStudents(filterByMark(groupmates, mark));
}
