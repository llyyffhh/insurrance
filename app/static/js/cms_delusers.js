
$(document).ready(function () {
    $("a[name='del']").click(function (event) {
        event.preventDefault();
        $
        var url = $("a[name='del']").attr('href');
        $.ajax({
            type:'GET',
            url : url,
            dataType :'json',
            success:function (data) {
                if(data['code']==200){
                    alert.alertSuccess('删除成功!',function () {
                        location.reload(true);
                    });

                }else{
                    alert.alertInfoToast(data['msg'])
                }
                
            }
        })
    })
});