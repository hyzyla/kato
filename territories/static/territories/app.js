$(document).ready(function () {
    const API_URL = "/api/territories/";
    const CLOSED_MARKER = '<i class="territory-list-marker bi bi-caret-right-fill"></i>';
    const OPENED_MARKER = '<i class="territory-list-marker bi bi-caret-down-fill"></i>';
    const EMPTY_MARKER = '<i class="territory-list-marker"></i>';

    function createList(data) {
        const items = data.results;
        const list = $(`<div class="list-group"/>`);
        const listItems = items.map(function (item) {
            const line = $(`<div class="list-group-item">${item.name}</div>`)
            // if (item.children_count > 0) {
            //     line.find('.territory-name-icon')
            //         .prepend(CLOSED_MARKER)
            //         .click(openItem)
            //         .addClass('territory-name-icon-clickable');
            // } else {
            //     line.find('.territory-name-icon')
            //         .prepend(EMPTY_MARKER);
            // }
            return $(`<li id="${item.code}" class="list-group-item"/>`).append(line);
        });
        list.append(listItems);
        return list;
    }

    function openItem(event) {
        const target = $(this);
        const parent = target.closest('li');
        const code = parent.attr('id');
        $(parent).find('.list-icon').replaceWith(OPENED_MARKER);
        $.ajax({
            url: API_URL,
            type: "get",
            data: { parent: code },
        })
        .done(function (data) {
            const list = createList(data);
            $(parent).append(list);
            $(target).unbind('click').click(closeItem);
        });

    }

    function closeItem(event) {
        const parent = $(this).closest('li');
        $(parent).find('.list-icon').replaceWith(CLOSED_MARKER);
        $(parent).children('span').children('.marker').remove();
        $(parent).children('ul').remove();
        $(this).unbind('click').click(openItem);

    }
    $.ajax({
        url: API_URL,
        type: "get",
        data: { level: 1 },
    })
    .done(function (data) {
        const list = createList(data);
        $('#list-root').append(list)
    });
});
