from django.shortcuts import render,redirect
from .models import Group,Module,Host,Args
from .adhoc2 import adhoc

# Create your views here.

def index(request):
    return  render(request,'webadmin/serverinfo.html')

def wadd_hosts(request):
    # get or post , to excute different tings
    if request.method=='POST':
        g = request.POST.get('group').strip()
        h = request.POST.get('hostname').strip()
        i = request.POST.get('ip').strip()
        if g:
            group = Group.objects.get_or_create(groupname=g)[0]
            if h and i :
                group.host_set.get_or_create(hostname=h,ipaddr=i)


    groups=Group.objects.all()
    return  render(request,'webadmin/add_hosts.html',{'groups':groups})

def add_modules(request):
    # print(dir(request))
    # print(request.method)
    # print(request.POST)
    # print(request.GET)
    if request.method=="POST":
        m = request.POST.get('module').strip()
        p = request.POST.get('param').strip()
        if m:
            module=Module.objects.get_or_create(modulename=m)[0]
            if p:
                module.args_set.get_or_create(args_text=p)
    modules = Module.objects.all()
    return render(request,'webadmin/add_modules.html',{'modules':modules})

def tasks(request):
    if request.method=='POST':
        ip = request.POST.get('host')
        group=request.POST.get('group')
        module=request.POST.get('module')
        args=request.POST.get('args')
        if group:
            dest=group
        elif ip:
            dest=ip
        else:
            dest=None
        if dest:
            if module and args:
                adhoc(['ansi_cfg/dhost.py'],dest,module,args)

    hosts=Host.objects.all()
    groups=Group.objects.all()
    modules=Module.objects.all()
    # print(hosts)
    # print(groups)
    # print(modules)
    objs={'hosts':hosts,'groups':groups,'modules':modules}
    # print(objs)
    return render(request,'webadmin/tasks.html',{'objs':objs})

def del_args(request,args_id):
    args=Args.objects.get(id=args_id)
    args.delete()

    return  redirect('add_modules')