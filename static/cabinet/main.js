$(document).ready(function () {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        var host = document.location.host;
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // ------------------------------- Loader -------------------------------
    var loader = $('#loader');
    function startLoader(){
        loader.css({
            display: 'flex'
        })
    }

    function endLoader(){
        loader.css({
            display: 'none'
        })
    }


    // ------------------------------- Регистрация ребёнка -------------------------------

    $('#child-register-form, #editProfileForm').find('input').each(function () {
        $(this).addClass('form-control');
    });

    // ------------------------------- Таблица клубов в кабинете -------------------------------

    if ($.fn.DataTable) {
        $('#clubsTableCabinet').DataTable({
            language: {
                "processing": "Подождите...",
                "search": "Поиск:",
                "lengthMenu": "Показать _MENU_ записей",
                "info": "Записи с _START_ до _END_ из _TOTAL_ записей",
                "infoEmpty": "Записи с 0 до 0 из 0 записей",
                "infoFiltered": "(отфильтровано из _MAX_ записей)",
                "infoPostFix": "",
                "loadingRecords": "Загрузка записей...",
                "zeroRecords": "Записи отсутствуют.",
                "emptyTable": "В таблице отсутствуют данные",
                "paginate": {
                    "first": "Первая",
                    "previous": "Предыдущая",
                    "next": "Следующая",
                    "last": "Последняя"
                },
                "aria": {
                    "sortAscending": ": активировать для сортировки столбца по возрастанию",
                    "sortDescending": ": активировать для сортировки столбца по убыванию"
                }
            }
        });
    }


    // ------------------------------- Расписание занятий в группе -------------------------------

    if ($.fn.fullCalendar) {
        $('#calendar').fullCalendar({
            header: {
                left: 'prev,next today',
                center: 'title',
                right: 'month,agendaWeek,agendaDay,listWeek'
            },
            navLinks: true,
            editable: false,
            eventLimit: true,
            eventSources: [
                {
                    url: window.location.href,
                    method: 'POST'
                }
            ]
        });
    }

    // ------------------------------- Добавление события в расписание -------------------------------

    var modal = $('#cabinetModal');

    $('#scheduleAddEvent').click(function (e) {
        e.preventDefault();
        var url = $(this).attr('href');

        $.ajax({
            url: url,
            method: 'get',
            success: function (r) {
                $('#cabinetModal > .modal-dialog').html(r);
                $(document).find('.date-picker').datetimepicker();
                modal.modal('show');
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    // ------------------------------- красивые поля input[type='number'] -------------------------------
    // Docs http://dimox.name/jquery-form-styler/

    if ($.fn.styler) {
        $('.input_styler').styler();
    }

    // ------------------------------- Пересчёт количества товаров в корзине -------------------------------

    function cartRecount() {
        var totalRow = 0,
            totalCart = 0;
        $.each($('.cartRow'), function (index, value) {
            var rowQuantity = parseInt($(value).find('input.cart-quantity').val()),
                rowPrice = parseFloat($(value).find('.cartRowPrice').text());
            totalRow = rowPrice * rowQuantity;
            totalCart += totalRow;
            $(value).find('.cartRowTotal').text(totalRow.toFixed(2));
            totalRow = 0;
        });
        $('#cartTotal').text(totalCart.toFixed(2));
    }

    var saveCartBtn = $('#saveCartBtn'),
        cartCheckoutBtn = $('#cartCheckoutBtn'),
        productQuantityInput = $('input.cart-quantity'),
        form = $('#cartForm');

    productQuantityInput.on('change, input', function () {
        saveCartBtn.show();
        cartCheckoutBtn.hide();
        cartRecount();
    });

    saveCartBtn.click(function (e) {
        e.preventDefault();
        $.ajax({
            url: window.location.href,
            data: form.serialize(),
            method: 'post',
            success: function (response) {
                if (response.status) {
                    saveCartBtn.hide();
                    cartCheckoutBtn.show();
                }
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    if ($.fn.datetimepicker) {
        console.log();
        $('.dateInput').find('input').datetimepicker({
            maxDate: Date.now(),
            format: 'DD.MM.Y'
        });
    }


    // ------------------------------- ??? -------------------------------

    $('#currency-select').on('change', function () {
        var currency = $(this).val();
        startLoader();
        $.ajax({
            url: window.location.href,
            data: {currency: currency},
            method: 'post',
            success: function (response) {
                var contentWrapper = $('#contentWrapper');
                contentWrapper.html(response);
                endLoader();

                var currencyAmount = contentWrapper.find('#currencyAmount');
                var token_course = parseFloat(contentWrapper.find('.coin-course').text());
                var course = parseFloat(contentWrapper.find('#currensyCourse').text());

                $(currencyAmount).on('change, input', function () {
                    var amount = parseFloat($(this).val());
                    var tokenAmount = ((amount * course)/token_course).toFixed(7);
                    var bonus = (tokenAmount * .03).toFixed(0);
                    contentWrapper.find('#ico__you-get__amount').text(tokenAmount);
                    contentWrapper.find('#ico__you-get__bonus').text(bonus);
                });

            },
            error: function () {
                alert('Oops! It was error!');
                endLoader();
            }
        });
    });


});
