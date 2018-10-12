

$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();

        var selectInput = $('#permission').val();
        var UserId =$('#submit').attr('data-user-id');
        zlajax.post({
            'url' : '/user/edit_user'+'?user_id='+UserId,
            'data': {
                'permission':selectInput
            },
            'success':function (data) {
                if(data['code']==200){
                    alert.alertSuccess('用户信息修改成功！');
                }else {
                    alert.alertInfoToast(data['msg']);
                }
            }

        })

    });
});



