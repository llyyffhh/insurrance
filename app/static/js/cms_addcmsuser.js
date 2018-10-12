/**
 * Created by Administrator on 2017/3/18.
 */

$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();

        var loginNameInput = $('input[name=login_name]');
        var usernameInput = $('input[name=name]');
        // var passwordInput = $('input[name=password]');
        var selectedCheckbox = $(':checkbox:checked');

        var loginName = loginNameInput.val();
        var username = usernameInput.val();
        // var password = passwordInput.val();
        var roles = [];
        selectedCheckbox.each(function (index,element) {
            var role_id = $(this).val();
            roles.push(role_id);
        });

        if(!loginName){
            alert.alertInfoToast('请输入登录名');
            return;
        }

        zlajax.post({
            'url': '/user/add_user',
            'data': {
                'login_name': loginName,
                'name': username,
                // 'password': password,
                'roles': roles
            },
            'success': function (data) {
                if(data['code'] == 200){
                    loginNameInput.val('');
                    usernameInput.val('');
                    // passwordInput.val('');
                    // 取消选中checkbox
                    selectedCheckbox.each(function () {
                       $(this).prop('checked',false);
                    });
                    alert.alertSuccessToast('恭喜！CMS用户添加成功！');
                }else{
                    alert.alertInfoToast(data['msg']);
                }
            }
        })
    });
});
