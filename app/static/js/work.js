$(document).ready(function () {
        $('#table').bootstrapTable({
            url: '/work',
            queryParamsType: '',              //默认值为 'limit' ,在默认情况下 传给服务端的参数为：offset,limit,sort
            queryParams: queryParams,
            method: "post",
            clickToSelect : true,
            editable:true,
            pagination: true,
            pageNumber: 1,
            pageSize: 10,
            pageList: [10, 20, 50, 100],
            sidePagination: "server",         //分页方式：client客户端分页，server服务端分页（*）
            striped: true,                    //是否显示行间隔色
            cache: false,
            uniqueId: "Id",               //每一行的唯一标识，一般为主键列
            height:300,
            paginationPreText: "上一页",
            paginationNextText: "下一页",
            columns: [
                {checkbox : true},
                { title: '序号', width: 50, align: "center", formatter: function (value, row, index) { return index + 1; } },
                { title: '姓名', field: 'name'},
                { title: '身份证号',field: 'num'},
                { title: '年龄',field : 'age'},
                { title: '手机号', field: 'tel'},
                { title: '低保', field: 'low',},
                { title: '缴费状态', field :'state'},
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
    function SearchData() {
        $('#table').bootstrapTable('refresh', { pageNumber: 1 });
    }


    $(function() {
    $( "#dialog-modal" ).dialog({
      modal: false
    });
  });





    //缴费
    function Pay(){
        var opts = $('#table').bootstrapTable('getSelections');
        if (opts == "") {
            alert.alertInfo("请选择要缴费的人员");
        }else{
        alert.alertOneInput({
        'title':'请输入缴费金额',
        'placeholder': '单位(元)',
        'confirmCallback':function () {

                    var opts = $('#table').bootstrapTable('getSelections')[0];
                    var name = opts.name;
                    var num = opts.num;
                    var tel = opts.tel;
                    var money = data;
                    var low = opts.low;
                    console.log(opts);
                    zlajax.post({
                        'url': '/pay',
                        'data': {
                            'name': name,
                            'num': num,
                            'tel': tel,
                            'money': money,
                            'low':low
                        },
                        'success': function (data) {
                            if (data['code'] == 200) {
                                alert.alertSuccess(msg = '缴费成功！');
                                $('#query').click()
                            }else{
                                alert.alertInfo(msg=data['msg']);
                            }
                        }
                    })


    }
})
    }
    }


    $(document).keydown(function(event){
    if(event.keyCode == '13'){
        $('#query').click();
    }
});



$(function () {
    $("#add-data").click(function (event) {
        var dialog = $("#add-dialog");
        dialog.modal("show");
        });
});

$(function () {
    $("#save-btn").click(function (evnet) {
        var dialog = $("#add-dialog");
        var nameInput = $("input[name='add-name']");
        var numInput = $("input[name='add-num']");
        var moneyInput = $("input[name='add-money']");
        var telInput = $("input[name='add-tel']");

        var name = nameInput.val();
        var num = numInput.val();
        var money = moneyInput.val();
        var tel = telInput.val();
        var low = $("#add-low option:selected").val();

        if(!name || !num || !money || !low){
            alert.alertInfoToast('请输入完整的数据！');
            return;
        }

        zlajax.post({
            'url':'add_data',
            'data':{
                'name':name,
                'num':num,
                'money':money,
                'tel': tel,
                'low':low
            },
            "success": function (data) {
                if(data['code']==200){
                    dialog.modal("hide");
                    alert.alertSuccess(msg='添加成功!');
                    $('#data')[0].reset();
                }else{
                    alert.alertInfo(msg=data['msg']);
                }
            },
            'fail':function () {
                alert.alertNetworkError();
            }
        });
    })
});






