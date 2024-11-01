import React, { useState } from 'react';
import { Button, Form, Input, Row, Col } from 'antd';

type LayoutType = Parameters<typeof Form>[0]['layout'];

const LoginPage: React.FC = () => {
  const [form] = Form.useForm();
  const [formLayout, setFormLayout] = useState<LayoutType>('vertical');

  const onFormLayoutChange = ({ layout }: { layout: LayoutType }) => {
    setFormLayout(layout);
  };

  const onFinish = (values: any) => {
    console.log('Success:', values);
  };

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <Row justify="center" align="middle" style={{ height: '100vh' }}>
      <Col xs={24} sm={16} md={12} lg={8} xl={6}>
        <h2 style={{textAlign: 'center', fontWeight: '500'}}>Bem-vindo ao Dephgo</h2>
        <Form
          layout={formLayout}
          form={form}
          initialValues={{ layout: formLayout }}
          onValuesChange={onFormLayoutChange}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          style={{ maxWidth: '100%' }}
        >
          <Form.Item
            label="E-mail"
            name="email"
            rules={[
              { required: true, message: 'Por favor, insira seu e-mail!' },
              { type: 'email', message: 'Por favor, insira um e-mail válido!' }
            ]}
          >
            <Input size='large' placeholder="Example@dominio.com" />
          </Form.Item>
          <Form.Item
            label="Senha"
            name="password"
            rules={[{ required: true, message: 'Por favor, insira sua senha!' }]}
          >
            <Input size='large' type='password' placeholder="Digite sua senha" />
          </Form.Item>
          <Form.Item style={{ textAlign: 'center' }}>
            <Button style={{margin: '8px 0'}}  size='large' block type="primary" htmlType="submit">Entrar</Button>
          </Form.Item>
        </Form>
      </Col>
    </Row>
  );
};

export default LoginPage;