$(document).ready(function () {
    $('#detail').click(function () {
        $('#table').bootstrapTable({
            url: '/today_detail',
            queryParamsType: '',              //默认值为 'limit' ,在默认情况下 传给服务端的参数为：offset,limit,sort
            queryParams: queryParams,
            method: "post",
            clickToSelect: true,
            editable: true,
            pagination: true,
            pageNumber: 1,
            pageSize: 10,
            pageList: [10, 20, 50, 100],
            sidePagination: "server",         //分页方式：client客户端分页，server服务端分页（*）
            striped: true,                    //是否显示行间隔色
            cache: false,
            uniqueId: "Id",               //每一行的唯一标识，一般为主键列
            height: 500,
            paginationPreText: "上一页",
            paginationNextText: "下一页",
            columns: [
                {
                    title: '序号', width: 50, align: "center", formatter: function (value, row, index) {
                        return index + 1;
                    }
                },
                {title: '姓名', field: 'name'},
                {title: '身份证号', field: 'num'},
                {title: '缴费金额', field: 'money'},
                {title: '年龄', field: 'age'},
                {title: '手机号', field: 'tel'},
                {title: '低保', field: 'low',},
                {title: '新增', field: 'new'},
                // {
                //     title: '操作', field: 'BookId', formatter: function (value, row, index) {
                //         var html = '<button class="btn btn-success btn-xs" data-toggle="modal" data-target="#pay">\n' +
                //             '缴费' +
                //             '</button>';
                //         html += '　<a href="javascript:Edit(' + value + ')" class="btn btn-danger btn-xs" >修改</a>';
                //         return html;
                //     }
                // }
            ],

        });
    });
});

    //查询条件
    function queryParams(params) {
        return {
            pageSize: params.pageSize,
            pageIndex: params.pageNumber,
            num: $.trim($("#num").val()),
            name: $.trim($("#name").val())
        };
    }

    //查询事件
    function query() {
        $('#table').bootstrapTable('refresh', { pageNumber: 1 });
    }