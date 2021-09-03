# 클래스 생성
class Post:
  """
  게시물 클래스
  param id: 글번호
  param title: 글제목
  param content: 글내용
  param view_count: 조회수
  """

  # 초기화
  def __init__(self, id, title, content, view_count):
    self.id = id
    self.title = title
    self.content = content
    self.view_count = view_count

  # 게시물 수정 메서드
  def set_post(self, id, title, content, view_count):
    self.id = id
    self.title = title
    self.content = content
    self.view_count = view_count

  # 뷰 카운트 증가 메서드
  def add_view_count(self):
    self.view_count += 1

  # 속성값 반환 메서드 (id)
  def get_id(self):
    return self.id
  
  # 속성값 반환 메서드 (title)
  def get_title(self):
    return self.title

  # 속성값 반환 메서드 (content)
  def get_content(self):
    return self.content
  
  # 속성값 반환 메서드 (view_count)
  def get_view_count(self):
    return self.view_count

# 모듈안에서 테스트
if __name__ == "__main__":
  # post 인스턴스 생성
  post = Post(1, "테스트", "테스트 입니다.", 0)
  # post.set_post(1, "테스트2", "테스트 2입니다.", 0)
  post.add_view_count()

  # post 속성 값 확인
  print(f"{post.get_id()} {post.get_title()} {post.get_content()} {post.get_view_count()}")

  
