
// document.getElementsByClassName('form_order')[0].submit()
// заполняе  плейсхолдеры в инпутах календарей

var serch_input1 = document.getElementsByClassName('datetimepicker-input')[0].placeholder = 'Дата дедлайна';
var serch_input = document.getElementsByClassName('datetimepicker-input')[1].placeholder = 'Фильтр по дате дедлайна';

console.log(serch_input)

//<!-- datetimepicker-->
$(function () {
    $("#datetimepicker1").datetimepicker({
        format: 'DD-MM-YYYY ', /*'DD-MM-YYYY HH:mm', отключили часы*/
        locale: 'ru',
    });
});
$(function () {
    $("#datetimepicker2").datetimepicker({
        format: 'DD-MM-YYYY', /*'DD-MM-YYYY HH:mm', отключили часы*/
        locale: 'ru',
    });
});

//<!--end datetimepicker-->
// Пример стартового JavaScript для отключения отправки форм при наличии недопустимых полей
(function () {
    'use strict'

    // Получите все формы, к которым мы хотим применить пользовательские стили проверки Bootstrap
    var forms = document.querySelectorAll('.needs-validation')

    // Зацикливайтесь на них и предотвращайте отправку
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }

                form.classList.add('was-validated')
            }, false)
        })
})()