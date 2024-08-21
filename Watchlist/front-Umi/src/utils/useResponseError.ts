import lodash from 'lodash';
import { App } from 'antd';

/**
 * 处理返回值异常
 * 根据 error 处理异常
 *
 * 在 model 使用时需要通过 console 输出错误
 * 在组件中使用时，可通过 message 输出错误
 */
export function useResponseError() {

  const { message: m } = App.useApp();
  const showError = (error: any, inConsole = false) => {

    let errStr = '[response error]';

    if (lodash.has(error, 'response.data.message')) {
      // 自定义 Response Error
      errStr += `code:${lodash.get(error, 'response.data.code')} message:${lodash.get(error, 'response.data.message')}`;
    } else if (lodash.has(error, 'message')) {
      // Axios Error
      errStr += lodash.get(error, 'message');
    } else {
      //  其他
      errStr += '程序内部错误！';
    }

    // 组件内可以使用 message 输出错误信息
    // 组件外只能使用 console.error 输出错误信息
    if (inConsole) {
      console.error(errStr, error);
    } else {
      m.error(errStr).then();

    }
  };


  return {
    showError,
  };

}