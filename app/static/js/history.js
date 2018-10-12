$(document).ready(function () {
    $('#query-data').click(function () {
        $('#table').bootstrapTable({
            url: '/history_detail',
            queryParamsType: '',              //默认值为 'limit' ,在默认情况下 传给服务端的参数为：offset,limit,sort
            queryParams: queryParams,
            method: "post",
            clickToSelect: true,
            pagination: true,
            pageNumber: 1,
            pageSize: 'all',
            pageList: [10, 20, 50, 100],
            sidePagination: "server",         //分页方式：client客户端分页，server服务端分页（*）
            striped: true,                    //是否显示行间隔色
            cache: false,
            uniqueId: "Id",               //每一行的唯一标识，一般为主键列
            height: 500,
            paginationPreText: "上一页",
            paginationNextText: "下一页",
            showExport: true,
            exportDataType: 'all',
            exportTypes: ['excel', 'xlsx'],
            exportOptions: {
                filename: '医疗保险数据导出',
                worksheetName: 'Sheet1',
                tableName: '数据表'
            },
            columns: [
                {checkbox: true},
                {
                    title: '序号', width: 50, align: "center", formatter: function (value, row, index) {
                        return index + 1;
                    }
                },
                {
                    title: '姓名', field: 'name', editable: {
                        type: 'text', validate: function (value) {
                            if ($.trim(value) == '') {
                                return '姓名不能为空!';
                            }
                        }
                    }
                },
                {
                    title: '身份证号', field: 'num', editable: {
                        type: 'text', validate: function (value) {
                            if ($.trim(value) == '') {
                                return '身份证号不能为空!';
                            }
                        }
                    }
                },
                {
                    title: '缴费金额', field: 'money', editable: {
                        type: 'text', validate: function (value) {
                            if ($.trim(value) == '') {
                                return '金额不能为空!';
                            }
                        }
                    }
                },
                {title: '年龄', field: 'age'},
                {
                    title: '手机号', field: 'tel', editable: {
                        type: 'text', validate: function (value) {
                            if ($.trim(value) == '') {
                                return '手机号不能为空!';
                            }
                        }
                    }
                },
                {
                    title: '低保', field: 'low', editable: {
                        type: 'select', source: [{value: 0, text: '否'}, {value: 1, text: '是'}]
                    }
                },
                {
                    title: '新增', field: 'new', editable: {
                        type: 'select', source: [{value: 0, text: '否'}, {value: 1, text: '是'}]
                    }
                },
                {title: '缴费时间', field: 'join_time'},
                // {
                //     title: '操作', field: 'BookId', formatter: function (value, row, index) {
                //         var html = '<button class="btn btn-success btn-xs" data-toggle="modal" data-target="#pay">\n' +
                //             '修改' +
                //             '</button>';
                //         html += '　<a href="javascript:deleteInfo(' + value + ')" class="btn btn-danger btn-xs" id="delete">删除</a>';
                //         return html;
                //     }
                // }
            ],
            onEditableSave: function (field, row, oldValue, $el) {
                $.ajax({
                    type: 'post',
                    url: '/edit',
                    data: row,
                    dataType: 'JSON',
                    success: function (data) {
                        if (data['code' == 200]) {
                            alert.alertSuccess('修改成功');
                        } else {
                            alert.alertInfo(msg = code['msg'])
                        }
                    },
                    error: function () {
                        alert.alertInfo('修改失败');
                    },
                    complete: function () {

                    }
                })
            }

        });
    });
});

    //查询条件
    function queryParams(params) {
        return {
            pageSize: params.pageSize,
            pageIndex: params.pageNumber,
            num: $("input[id='num']").val(),
            name: $("input[id='name']").val(),
            date: $(".form_datetime").find('input').val()
        };
    }

    //查询事件
    function query() {
        $('#table').bootstrapTable('refresh', { pageNumber: 1 });
    }
    function deleteInfo(){
        if (confirm("确认要删除吗？")) {
            var idlist = $('#table').bootstrapTable('getSelections')[0];
            var name = idlist.name;
            var num = idlist.num;
            zlajax.post({
                'url': '/delete',
                'data': {
                    'name':name,
                    'num':num
                },
                'success': function (data) {
                    if(data['code']==200){
                        alert.alertSuccess('删除成功!');
                        query()
                    }else{
                        alert.alertInfo(msg=code['msg'])
                    }
                }
            })

        }
    }

    $(function () {
    $("#edit-data").click(function (event) {
        var dialog = $("#edit-dialog");
        dialog.modal("show");
        var idlist = $('#table').bootstrapTable('getSelections')[0];
            $('#edit-name').val(idlist.name);
            $('#edit-num').val(idlist.num);
            $('#edit-tel').val(idlist.tel);
            $('#edit-money').val(idlist.money);
        });
});
    $(function () {
        $("#save-btn").click(function (evnet) {
            var dialog = $("#add-dialog");
            var nameInput = $("input[name='edit-name']");
            var numInput = $("input[name='edit-num']");
            var moneyInput = $("input[name='edit-money']");
            var telInput = $("input[name='edit-tel']");
            var name = nameInput.val();
            var num = numInput.val();
            var money = moneyInput.val();
            var tel = telInput.val();
            var low = $("#edit-low option:selected").val();
            if(!name || !num || !money || !low){
            alert.alertInfoToast('请输入完整的数据！');
            return ;
        }

        zlajax.post({
            'url':'/edit',
            'data':{
                'raw_name': $('#table').bootstrapTable('getSelections')[0].name,
                'raw_num': $('#table').bootstrapTable('getSelections')[0].num,
                'raw_money': $('#table').bootstrapTable('getSelections')[0].money,
                'raw_tel': $('#table').bootstrapTable('getSelections')[0].tel,
                'raw_low': $('#table').bootstrapTable('getSelections')[0].low,
                'name':name,
                'num':num,
                'money':money,
                'tel': tel,
                'low':low
            },
            "success": function (data) {
                if(data['code']==200){
                    dialog.modal("hide");
                    alert.alertSuccess(msg='修改成功!');
                    $('#data')[0].reset();
                    query()
                }else{
                    alert.alertInfo(msg=data['msg']);
                }
            },
            'fail':function () {
                alert.alertNetworkError();
            }
        });

        });
    });
