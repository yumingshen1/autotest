yaml使用场景：
    1- 做配置文件
    2- 做测试用例
    
配置文件：
    开发角度：
        1- 现成的第三方组件
            tomcat---tomcat/conf/server.xml 
                修改常见配置：连接数 端口  webpath  staticSourcePath
            mysql---my.cnf  
                端口  log  buffer  连接数等
            redis---redis.cnf
                端口 连接池等  内存模式 0,1,2
        2- 项目的配置文件
            1- xxx.properties---jmeter.properties
            2- xxx.ini-----pytest.ini
            3- xxx.cnf
            4- xxx.xml
            5- xxx.yml
                1- springboot开发框架
                2- springCloud微服务架构
                3- 微服务的k8s集群使用yml格式的配置文件
                
    测试角度：
        1- 公司没有运维，测试人员很可能会充当一部分运维工作
        2- 性能测试---很多监控与项目配置文件一定看得懂，会修改一些参数
        3- 自动化测试做配置文件  apiPath.yml
        4- 自动化测试用例

#yaml里引用yaml文件      
import yaml
import os.path
class Loader(yaml.Loader):#继承
    def __init__(self, stream):
        self._root = os.path.split(stream.name)[0]
        super(Loader, self).__init__(stream)
    def include(self, node):
        filename = os.path.join(self._root, 			self.construct_scalar(node))
        with open(filename, 'r') as f:
            return yaml.load(f, Loader)
Loader.add_constructor('!include', Loader.include)
            
        