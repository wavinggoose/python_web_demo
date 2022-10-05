# 1.导入模型类
from django.http import HttpResponse

from myapp.models import UserInfo


def add_user(request):
    # 2.使用模型类对数据库进行操作
    # 添加数据(第一种方式)
    # 1.添加的数据到哪一张表中,就是用哪一张表的模型类
    # 2.模型类.objects.create(字段名=字段的值)
    UserInfo.objects.create(
        username='小明',
        password='123456',
        email='123456@qq.com',
        sex='男'
    )
    return HttpResponse('插入成功')


def add_user_2(request):
    # 第二种方式插入数据
    # 根据模型类创建对象
    user = UserInfo(
        username='小红',
        password='123',
        email='xh@qq.com',
        sex='女'
    )
    # 将对象保存到数据库中
    user.save()
    return HttpResponse('插入成功')


def delete_user(request):
    # 删除UserInfo表中所有性别为男的数据
    # 1.删除哪一张表的数据,就使用哪一张表的模型类
    # 2.通过filter(条件)筛选出符合条件的数据 返回一个QuerySet类型
    # QuerySet类型可以看作是一个列表,列表中的内容就是一个一个的对象
    # [对象1(第一条数据),对象2(第二条数据),对象3(第三条数据),........]
    # 3.通过delete()删除指定的数据
    users = UserInfo.objects.filter(sex='男')
    users.delete()
    return HttpResponse('删除成功')


def delete_user_2(request):
    # UserInfo.objects.filter(sex='男').delete()
    # 删除id为30的数据
    UserInfo.objects.filter(id=30).delete()
    return HttpResponse('删除成功')


def update_user(request):
    # 第一种方式,修改多条数据
    # 1.修改哪一张表的数据,就使用哪一张表的模型类
    # 2.通过filter(条件)筛选出符合条件的数据
    # 3.通过update(要修改的字段名=新的值)进行修改
    # 修改UserInfo表中所有性别为男的数据,将他们的password改为hhh
    UserInfo.objects.filter(sex='男').update(password='hhh')
    # 通过第一种方式进行修改的数据不会更新最后修改时间
    # 修改用户名为小明并且密码为123的数据,将这条数据的邮箱修改为xm@163.com
    UserInfo.objects.filter(username='小明',password='123').update(email='xm@163.com')
    return HttpResponse('修改成功')


def update_user_2(request):
    # 第二种方式,修改一条数据
    # 1.修改哪一张表的数据,就使用哪一张表的模型类
    # 2.通过get(条件)获取指定的数据,返回值是一个对象(条件必须是唯一的)
    # 3.修改对象的属性
    # 4.执行save()方法
    # 修改id为31的数据,将username改为小芳,性别改为男
    user = UserInfo.objects.get(id=33)
    user.username = '小芳'
    user.sex = '男'
    user.save()
    return HttpResponse('修改成功')


def query_user(request):
    # 1.查询多条数据:返回值类型为QuerySet,可以将它看作是一个列表
    # [对象1,对象2,对象3,......]其中对象对应的是一条数据
    # 对象中的属性就是一条数据中的某个字段
    # (1)查询表中所有数据
    # 查哪一张表,就使用哪一张表的模型类
    user_list = UserInfo.objects.all()

    # (2)查询指定的数据filter(条件1,条件2,......)
    # 如果不写条件,就是查询所有数据
    # (2.1)查询某个某个字段等于某个值的情况
    # 查询性别为'女'的数据
    user_list = UserInfo.objects.filter(sex='女')

    # (2.2)查询某个字段包含某个值的情况
    # 查询用户名中包含'1'的数据
    user_list = UserInfo.objects.filter(username__contains='1')

    # (2.3)查询某个字段的值等于指定好的几个值
    # 查询用户名是'小红1'或者'小芳'的数据
    user_list = UserInfo.objects.filter(username__in=['小红1', '小芳'])

    # (2.4)查询某个字段值大于某个值的数据
    # 查询id大于35的数据
    user_list = UserInfo.objects.filter(id__gt=35)

    # (2.5)查询某个字段值小某个值的数据
    # 查询id小于10的数据
    user_list = UserInfo.objects.filter(id__lt=10)

    # (2.6)查询某个字段值介于某个区间中
    # 查询id大于10,小于30的数据
    user_list = UserInfo.objects.filter(id__gt=10, id__lt=30)
    # 查询id大于等于10,小于等于30的数据
    user_list = UserInfo.objects.filter(id__range=[10, 30])

    # (2.7)查询不符合条件的数据
    # 查询id不小于10的数据
    user_list = UserInfo.objects.exclude(id__lt=10)
    # 查询id小于10或者id大于30的数据
    user_list = UserInfo.objects.exclude(id__range=[10, 30])

    # (2.8)将数据进行排序
    # 查询用户名包含'小红'的数据,并且按照用户名进行升序排列,如果相同则按照密码进行升序排列
    # order_by(排序条件1,排序条件2,.....)先按排序条件1进行排序,如果相同,再按排序条件2进行排序
    # 如果排序条件都相同,则按照先后顺序进行排序
    user_list = UserInfo.objects.filter(username__contains='小红').order_by('username', 'password')

    # 查询用户名包含'小红'的数据,并且按照用户名进行升序排列,如果相同则按照密码进行降序排列
    # 再排序条件前加'-'表示按照这个排序条件进行降序排列
    user_list = UserInfo.objects.filter(username__contains='小红').order_by('username', '-password')

    # (2.9)查询所有不重复的数据
    # 查询所有用户名为'小明'的不重复数据(重复数据返回一条)
    user_list = UserInfo.objects.filter(username='小明').distinct()

    # (2.10)查询指点列的数据（返回的类型是字典类型）  filter:指的是查询的数据   values:指的是指定范围的数据
    user_list = UserInfo.objects.filter(username__contains="大华").values('password', 'email')

    # （2，11）查询指定列的数据（返回的类型是元组类型）
    user_list = UserInfo.objects.filter(username__contains="小明").values_list('username', 'password', 'email')

    # 打印查询出来的数据
    print('*' * 100)
    for user in user_list:
        print(user)
    print('*' * 100)
    # 查询单条数据
    return HttpResponse('查询成功')
