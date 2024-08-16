declare namespace API {
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

  type UserRequest = {
    /** 用户名 创建用户时使用 */
    name: string;
  };

  type UserResponse = {
    /** 用户ID */
    id?: number;
    /** 用户名 */
    name?: string;
  };

  type ValidationError = {};
}
