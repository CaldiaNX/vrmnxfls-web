@echo off
: Python�̎��s���W���[���p�X���w��
SET PATH=%PATH%;C:\Python\Python39

: �e�|�[�g�Ɋ��蓖�Ă�HTTP�T�[�o���N���B
: �T�[�o���I������ꍇ�̓R�}���h�v�����v�g�����B
start python vrmnxfls_server_5301.py
start python vrmnxfls_server_5302.py
start python vrmnxfls_server_5303.py

: ���C�A�E�g�̗��ID��ݒ肵��Web�u���E�U���N���B
: ���ID��ύX�������ꍇ�́uslt1�v�̃p�����[�^��ύX�B
: �s�v�Ȃ瓪�Ɂurem �v��t���ăR�����g�A�E�g�B
: �O������̏ꍇ�́ulocalhost�v���O���[�o��IP�A�h���X�ɕύX����QR�R�[�h�Ȃǂŉ��L��URL��`����B
start http://localhost:5301/cgi-bin/vrmnxfls_controller.py?slt1=10
start http://localhost:5302/cgi-bin/vrmnxfls_controller.py?slt1=20
start http://localhost:5303/cgi-bin/vrmnxfls_controller.py?slt1=30

exit /b 0
