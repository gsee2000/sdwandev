FROM library/centos

RUN yum install -y man unzip epel-release git vim && yum clean all

RUN yum install -y python-pip bash-completion && yum clean all

RUN pip install --upgrade pip

RUN pip install ansible

RUN pip install vspk

RUN pip install ipython

ENTRYPOINT ["bash"]
