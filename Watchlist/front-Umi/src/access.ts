import { InitialStateType } from '@@/plugin-initialState/@@initialState';

export default function(initialState: InitialStateType) {

  return {
    hasLogin: () => {
      return initialState!.id !== -1;
    },
    notLogin: () => {
      return initialState!.id === -1;
    },
  };
}