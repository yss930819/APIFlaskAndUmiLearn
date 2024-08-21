declare namespace API {
  type AuthRequest = {
    /** 密码 登录时使用 */
    password: string;
    /** 用户名 登录时使用 */
    username: string;
  };

  type AuthResponse = {
    /** 令牌 登录成功后返回的令牌，在 Header 中增加  */
    access_token?: string;
  };

  type deleteMovieIdParams = {
    _id: number;
  };

  type deleteUserIdParams = {
    _id: number;
  };

  type Empty = {};

  type getHelloNameParams = {
    name: string;
  };

  type getMovieIdParams = {
    _id: number;
  };

  type getUserIdParams = {
    _id: number;
  };

  type HelloRequest = {
    /** 名称 返回消息会使用此名称 */
    name: string;
  };

  type HTTPError = {};

  type MovieRequest = {
    /** 电影名 */
    title: string;
    /** 年份 */
    year: string;
  };

  type MovieResponse = {
    /** 电影ID */
    id?: number;
    /** 电影名 */
    title?: string;
    /** 年份 */
    year?: string;
  };

  type putMovieIdParams = {
    _id: number;
  };

  type putUserIdParams = {
    _id: number;
  };

  type putUserIdPasswordParams = {
    _id: number;
  };

  type UserRequest = {
    /** 用户名 创建用户时使用 */
    name: string;
    /** 密码 创建用户时使用 */
    password: string;
    /** 用户名 创建用户时使用 */
    username: string;
  };

  type UserResponse = {
    /** 用户ID */
    id?: number;
    /** 用户名-显示 */
    name?: string;
    /** 用户名-登录 */
    username?: string;
  };

  type UserUpdatePasswordRequest = {
    /** 密码 */
    password: string;
  };

  type UserUpdateRequest = {
    /** 用户名 创建用户时使用 */
    name: string;
    /** 用户名 创建用户时使用 */
    username: string;
  };

  type ValidationError = {};
}
