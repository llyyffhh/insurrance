

$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();
        var oldpwdInput = $('input[name=old_pwd]');
        var newpwdInput = $('input[name=new_pwd]');
        var newpwdRepeatInput = $('input[name=new_pwd2]');

        var oldpwd = oldpwdInput.val();
        var newpwd = newpwdInput.val();
        var newpwd_repeat = newpwdRepeatInput.val();

        zlajax.post({
           'url': '/user/reset_pwd',
            'data': {
                'old_pwd': oldpwd,
                'new_pwd': newpwd,
                'new_pwd2': newpwd_repeat
            },
            'success': function (data) {
                if(data['code'] == 200){
                    oldpwdInput.val('');
                    newpwdInput.val('');
                    newpwdRepeatInput.val('');
                    alert.alertSuccessToast('恭喜您！密码修改成功！');
                }else{
                    alert.alertInfoToast(data['msg']);
                }
            },
            'fail': function (error) {
                // console.log(error);
                alert.alertNetworkError();
            }
        });
    });
});
